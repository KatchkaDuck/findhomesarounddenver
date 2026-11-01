#!/usr/bin/env python3
"""Renders print versions of the guides to dist/guides/*.pdf.

Content comes from the same src/pages files as the website, so the PDFs stay in
sync. Interactive calculators are replaced with a pointer to the live tool.
Run after build.py:  python3 src/make_pdfs.py
"""
import re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

DOMAIN = "https://findhomesarounddenver.com"
OUT = build.DIST / "guides"

GUIDES = {
    "sell": ("Seller's Guide", "seller-guide.pdf"),
    "buy": ("Buyer's Guide", "buyer-guide.pdf"),
    "moving-to-denver": ("Relocation Guide", "moving-to-denver-guide.pdf"),
}

PRINT_CSS = """
@page { size: Letter; margin: 0.85in 0.8in 0.9in; }
@page :first { margin: 0; }
html, body { background: #fff !important; }
:root { padding: 0 !important; }
body { font-size: 10.5pt; line-height: 1.55; color: #1a1a1f; }
.cover { height: 11in; background: #0c2749; color: #fff; display: grid; grid-template-rows: auto 1fr auto; padding: 0.9in 0.85in 0.8in; page-break-after: always; break-after: page; }
.cover .kicker { font-size: 9pt; letter-spacing: .2em; text-transform: uppercase; color: rgba(255,255,255,.7); font-weight: 600; }
.cover h1 { color: #fff; font-size: 48pt; line-height: 1; margin-top: 1.6in; max-width: 6in; }
.cover .lede { color: rgba(255,255,255,.8); font-size: 13pt; max-width: 5.2in; margin-top: 0.3in; }
.cover .who { display: flex; align-items: center; gap: 18px; }
.cover .who img.head { width: 1.1in; height: 1.1in; border-radius: 50%; object-fit: cover; object-position: 50% 25%; }
.cover .who b { display: block; font-family: var(--display); font-size: 17pt; font-weight: 500; }
.cover .who span { font-size: 9.5pt; color: rgba(255,255,255,.75); line-height: 1.5; }
.cover .logo { margin-left: auto; width: 0.95in; background: #fff; padding: 8px; border-radius: 10px; }
.article > section { padding: 0 0 22pt !important; border: 0 !important; break-inside: auto; }
.article > section + section { padding-top: 6pt !important; }
.article h2 { font-size: 24pt; margin: 0 0 10pt; break-after: avoid; }
.article h3 { font-size: 15pt; margin: 14pt 0 6pt; break-after: avoid; }
.article p, .article li { max-width: none; }
.list li, .steps li, .stat-row, .callout, tr { break-inside: avoid; }
.stat-row { margin: 12pt 0 6pt; }
.stat-row b { font-size: 20pt; }
.stat-row div { padding: 10pt; }
.callout { padding: 14pt 16pt; margin-top: 12pt; background: #f4f1eb; }
.callout blockquote { font-size: 14pt; }
.steps li { padding: 9pt 0; grid-template-columns: 34pt 1fr; }
.steps li::before { font-size: 18pt; }
.table-wrap { overflow: visible; border-radius: 8px; }
table { min-width: 0 !important; font-size: 9.5pt; }
th, td { padding: 7pt 9pt; }
.compare thead th { font-size: 12pt; }
.faq { max-width: none; }
.faq .qa { border-bottom: 1px solid #d6cfc3; padding: 9pt 0; break-inside: avoid; }
.faq .qa h3 { font-size: 13pt; margin: 0 0 4pt; }
.faq .qa p { color: #3b3832; padding: 0; }
.article > section#faq { break-before: page; }
.tool-note { background: #f4f1eb; border-radius: 10px; padding: 12pt 14pt; margin-top: 10pt; }
.closing { break-before: page; display: grid; gap: 14pt; }
.closing h2 { font-size: 26pt; }
.closing .card { display: flex; gap: 18px; align-items: center; background: #f4f1eb; border-radius: 14px; padding: 16pt; }
.closing .card img.head { width: 1in; height: 1in; border-radius: 50%; object-fit: cover; object-position: 50% 25%; }
.closing .card b { font-family: var(--display); font-size: 17pt; font-weight: 500; display: block; }
.closing .legal { font-size: 8pt; color: #5f5a52; border-top: 1px solid #d6cfc3; padding-top: 10pt; margin-top: 10pt; display: grid; gap: 6pt; }
.closing .legal .row { display: flex; align-items: center; gap: 12px; }
.closing .legal img { width: 0.7in; }
a { color: #0c2749; text-decoration: none; }
"""


def links_to_absolute(html):
    html = re.sub(r"\{\{link:index\}\}", DOMAIN + "/", html)
    html = re.sub(r"\{\{link:([a-z0-9-]+)\}\}", lambda m: f"{DOMAIN}/{m.group(1)}/", html)
    html = re.sub(r"\{\{asset:([^}]+)\}\}", lambda m: (ROOT / "assets" / m.group(1)).as_uri(), html)
    return html


def article_for_print(slug, body):
    art = body[body.index('<article class="article">'):body.rindex("</article>") + len("</article>")]
    # Calculators become a pointer to the live tool.
    start = art.find('<div class="calc"')
    if start != -1:
        depth, i = 0, start
        for m in re.finditer(r"<div\b|</div>", art[start:]):
            depth += 1 if m.group(0).startswith("<div") else -1
            if depth == 0:
                end = start + m.end()
                break
        note = (f'<div class="tool-note">Run your own numbers with the interactive calculator at '
                f'<a href="{DOMAIN}/{slug}/#calculator">findhomesarounddenver.com/{slug}</a>.</div>')
        art = art[:start] + note + art[end:]
    # FAQ accordions print open, as plain questions and answers.
    art = re.sub(r"<details[^>]*>\s*<summary>(.*?)</summary>\s*(.*?)</details>",
                 r'<div class="qa"><h3>\1</h3>\2</div>', art, flags=re.S)
    # "Keep reading" cards and download prompts are web-only.
    art = re.sub(r'<section id="next">.*?</section>', "", art, flags=re.S)
    art = re.sub(r'<section id="download">.*?</section>', "", art, flags=re.S)
    return links_to_absolute(art)


def page_html(slug, meta, body, label):
    lede = re.search(r'<p class="lede">(.*?)</p>', body, re.S).group(1)
    head = (ROOT / "assets" / "chris-portrait.jpg").as_uri()
    logo = (ROOT / "assets" / "remax-professionals.jpg").as_uri()
    css = (ROOT / "styles.css").read_text()
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{meta["headline"]}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<style>{css}{PRINT_CSS}</style></head><body>
<section class="cover">
  <p class="kicker">Find Homes Around Denver · {label} · {meta["updated"][:4]}</p>
  <div><h1>{meta["headline"]}</h1><p class="lede">{lede}</p></div>
  <div class="who"><img class="head" src="{head}" alt="">
    <div><b>Chris Nowakiwsky</b><span>Broker Associate · The Real Estate Experts<br>RE/MAX Professionals · (970) 485-2228<br>chris.nowakiwsky@remax.net</span></div>
    <img class="logo" src="{logo}" alt="RE/MAX Professionals"></div>
</section>
{article_for_print(slug, body)}
<section class="closing">
  <h2>Questions? Let's Talk.</h2>
  <p>Every move is different. If you'd like to talk through your plans, your neighborhood or your numbers, I'm happy to help, with no pressure and no obligation.</p>
  <div class="card"><img class="head" src="{head}" alt="">
    <div><b>Chris Nowakiwsky, Broker Associate</b>The Real Estate Experts · RE/MAX Professionals<br>(970) 485-2228 · chris.nowakiwsky@remax.net<br>findhomesarounddenver.com</div></div>
  <div class="legal">
    <div class="row"><img src="{logo}" alt="RE/MAX Professionals"><span>10111 Inverness Main St, Suite P, Englewood, CO 80112 · Colorado license #100090898</span></div>
    <p>Each RE/MAX office is independently owned and operated. Equal Housing Opportunity. Information in this guide is deemed reliable but not guaranteed and should be independently verified. Nothing here is legal, tax or financial advice. Updated {meta["updated"]}.</p>
  </div>
</section>
</body></html>'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "src" / ".pdf-tmp"
    tmp.mkdir(exist_ok=True)
    footer = ('<div style="width:100%;font:7.5pt Helvetica,Arial,sans-serif;color:#5f5a52;padding:0 0.8in;'
              'display:flex;justify-content:space-between"><span>Chris Nowakiwsky · RE/MAX Professionals · '
              'findhomesarounddenver.com</span><span><span class="pageNumber"></span></span></div>')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for slug, (label, fname) in GUIDES.items():
            meta, body = build.parse(build.SRC / f"{slug}.html")
            html_path = tmp / f"{slug}.html"
            html_path.write_text(page_html(slug, meta, body, label))
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.pdf(path=str(OUT / fname), format="Letter", print_background=True,
                     display_header_footer=True, header_template="<span></span>", footer_template=footer,
                     prefer_css_page_size=True)
            page.close()
            print("wrote", OUT / fname)
        browser.close()


if __name__ == "__main__":
    main()
