#!/usr/bin/env python3
"""Builds findhomesarounddenver.com from src/pages.

Two outputs from the same sources:
  preview/  ->  written to the site root (flat .html files, relative links)
                for the claude.ai design preview
  dist/     ->  the live site for Netlify (clean /slug/ URLs, live forms,
                sitemap.xml, robots.txt)

Each page in src/pages starts with a <!--meta {json} --> block, followed by the
<main> content. Inside content use {{link:slug}} for page links and
{{asset:file}} for files in assets/.
"""
import json, re, shutil, html
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "pages"
DIST = ROOT / "dist"
DOMAIN = "https://findhomesarounddenver.com"
TODAY = date.today().isoformat()

AGENT_ID = DOMAIN + "/#chris"
AGENT = {
    "@type": "RealEstateAgent",
    "@id": AGENT_ID,
    "name": "Chris Nowakiwsky, RE/MAX Professionals",
    "url": DOMAIN + "/",
    "image": DOMAIN + "/assets/chris-portrait.jpg",
    "logo": DOMAIN + "/assets/remax-professionals.jpg",
    "telephone": "+1-970-485-2228",
    "email": "chris.nowakiwsky@remax.net",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "10111 Inverness Main St, Suite P",
        "addressLocality": "Englewood",
        "addressRegion": "CO",
        "postalCode": "80112",
        "addressCountry": "US",
    },
    "parentOrganization": {"@type": "RealEstateAgent", "name": "RE/MAX Professionals"},
    "areaServed": [
        "Washington Park, Denver, CO", "Platt Park, Denver, CO", "Bonnie Brae, Denver, CO",
        "Belcaro, Denver, CO", "Cory-Merrill, Denver, CO", "South Park Hill, Denver, CO",
        "Sloan Lake, Denver, CO", "Capitol Hill, Denver, CO", "Hilltop, Denver, CO",
        "Greenwood Village, CO",
    ],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "bestRating": "5", "reviewCount": "8"},
    "sameAs": [
        "https://www.zillow.com/profile/chrisnowakiwsky",
        "https://thedenverexperts.com/agent/chris-nowakiwsky",
        "https://chris-nowakiwsky.homesbythepros.com/",
    ],
}
PERSON = {
    "@type": "Person",
    "@id": DOMAIN + "/#person",
    "name": "Chris Nowakiwsky",
    "jobTitle": "Broker Associate",
    "worksFor": {"@id": AGENT_ID},
    "url": DOMAIN + "/",
}

NAV = [
    ("sell", "Sell", "{{link:sell}}"),
    ("buy", "Buy", "{{link:buy}}"),
    ("moving", "Moving to Denver", "{{link:moving-to-denver}}"),
    ("neighborhoods", "Neighborhoods", "{{link:neighborhoods}}"),
    ("market", "Market", "{{link:index}}#market"),
    ("about", "About", "{{link:index}}#about"),
]
FOOTER_LINKS = [
    ("Sell Your Home", "{{link:sell}}"),
    ("Sell and Buy", "{{link:sell-and-buy}}"),
    ("Buy a Home", "{{link:buy}}"),
    ("First-Time Buyers", "{{link:first-time-buyers}}"),
    ("Moving to Denver", "{{link:moving-to-denver}}"),
    ("Neighborhoods", "{{link:neighborhoods}}"),
    ("Market Updates", "{{link:index}}#market"),
    ("About", "{{link:index}}#about"),
    ("Privacy Policy", "{{link:index}}#about"),
]

EHO_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8">'
           '<path d="M3 11 12 4l9 7v9H3z"/><path d="M8 13h8M8 16.5h8"/></svg>')


def header(nav_key):
    current = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{href}"{current if key == nav_key else ""}>{label}</a></li>'
        for key, label, href in NAV)
    return f'''<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="{{{{link:index}}}}">
      <strong>Chris Nowakiwsky</strong>
      <span>RE/MAX Professionals</span>
    </a>
    <ul class="nav-links">{items}</ul>
    <details class="mnav"><summary>Menu</summary><ul>{items}</ul></details>
  </nav>
</header>'''


def footer(legal_extra=""):
    links = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in FOOTER_LINKS)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <img class="footer-logo" src="{{{{asset:remax-professionals.jpg}}}}" width="360" height="358" alt="RE/MAX Professionals" loading="lazy">
      <div>
        <h3>Chris Nowakiwsky, Broker Associate</h3>
        <address>
          The Real Estate Experts · RE/MAX Professionals<br>
          10111 Inverness Main St, Suite P, Englewood, CO 80112<br>
          (970) 485-2228 · chris.nowakiwsky@remax.net<br>
          Colorado license #100090898
        </address>
      </div>
      <ul class="footer-links">{links}</ul>
    </div>
    <div class="legal">
      <span class="eho">{EHO_SVG}Equal Housing Opportunity</span>
      <p>Each RE/MAX office is independently owned and operated. Information on this site is deemed reliable but not guaranteed and should be independently verified. Nothing here is legal, tax or financial advice. {legal_extra}</p>
      <p>© {date.today().year} Chris Nowakiwsky, RE/MAX Professionals.</p>
    </div>
  </div>
</footer>'''


def valuation(slug, opts):
    """Home value request form, wired for Netlify Forms."""
    eyebrow = opts.get("eyebrow", "Free Home Valuation")
    heading = opts.get("heading", "What's Your Home Worth Today?")
    text = opts.get("text", "An automated estimate can miss by six figures in older neighborhoods. "
                            "Tell me about your home and I'll send a real valuation based on recent sales nearby, "
                            "usually within one business day.")
    placeholder = opts.get("placeholder", "123 S Gaylord St, Denver")
    timing = opts.get("timing", "Just curious")
    choices = ["Just curious", "In the next 3 months", "In 3 to 12 months", "Buying and selling at the same time"]
    options = "".join(f'<option{" selected" if c == timing else ""}>{c}</option>' for c in choices)
    return f'''<section class="band" id="value">
    <div class="wrap">
      <div class="cta">
        <div class="section-head" style="margin-bottom:0">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{heading}</h2>
          <p>{text}</p>
        </div>
        <form class="form" name="home-value" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-success="Thanks. Chris will send your home value within one business day." novalidate>
          <input type="hidden" name="form-name" value="home-value">
          <input type="hidden" name="page" value="{slug}">
          <p hidden><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
          <label for="v-address">Home address
            <input id="v-address" name="address" autocomplete="street-address" placeholder="{placeholder}" required>
          </label>
          <div class="row">
            <label for="v-name">Name
              <input id="v-name" name="name" autocomplete="name" required>
            </label>
            <label for="v-email">Email
              <input id="v-email" name="email" type="email" autocomplete="email" required>
            </label>
          </div>
          <div class="row">
            <label for="v-phone">Phone (optional)
              <input id="v-phone" name="phone" type="tel" autocomplete="tel">
            </label>
            <label for="v-timing">Timing
              <select id="v-timing" name="timing">{options}</select>
            </label>
          </div>
          <button class="btn btn-primary" type="submit">Get My Home Value</button>
          <p class="consent">By submitting, you agree Chris Nowakiwsky of RE/MAX Professionals may contact you about your request. No spam, and you can opt out anytime.</p>
          <p class="form-status" role="status"></p>
        </form>
      </div>
    </div>
  </section>'''


def contact(slug, opts):
    """General 'talk to Chris' form for buyer and relocation pages."""
    eyebrow = opts.get("eyebrow", "Talk to Chris")
    heading = opts.get("heading", "Start Your Home Search With a Plan")
    text = opts.get("text", "Tell me what you're looking for and when. I'll reply within one business day with next steps, "
                            "including homes worth a look and a lender or two I trust.")
    interest = opts.get("interest", "Buying a home")
    choices = ["Buying a home", "Buying my first home", "Moving to Denver", "Selling a home", "Selling and buying"]
    options = "".join(f'<option{" selected" if c == interest else ""}>{c}</option>' for c in choices)
    return f'''<section class="band" id="contact">
    <div class="wrap">
      <div class="cta">
        <div class="section-head" style="margin-bottom:0">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{heading}</h2>
          <p>{text}</p>
        </div>
        <form class="form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-success="Thanks. Chris will be in touch within one business day." novalidate>
          <input type="hidden" name="form-name" value="contact">
          <input type="hidden" name="page" value="{slug}">
          <p hidden><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
          <div class="row">
            <label for="c-name">Name
              <input id="c-name" name="name" autocomplete="name" required>
            </label>
            <label for="c-email">Email
              <input id="c-email" name="email" type="email" autocomplete="email" required>
            </label>
          </div>
          <div class="row">
            <label for="c-phone">Phone (optional)
              <input id="c-phone" name="phone" type="tel" autocomplete="tel">
            </label>
            <label for="c-interest">I'm interested in
              <select id="c-interest" name="interest">{options}</select>
            </label>
          </div>
          <label for="c-message">What are you looking for?
            <textarea id="c-message" name="message" rows="3" placeholder="Neighborhoods, price range, timing"></textarea>
          </label>
          <button class="btn btn-primary" type="submit">Send to Chris</button>
          <p class="consent">By submitting, you agree Chris Nowakiwsky of RE/MAX Professionals may contact you about your request. No spam, and you can opt out anytime.</p>
          <p class="form-status" role="status"></p>
        </form>
      </div>
    </div>
  </section>'''


def guide_download(slug, opts):
    """Email-gated PDF download, wired for Netlify Forms."""
    title, file = opts["title"], opts["file"]
    return f'''<section class="band tint" id="download">
    <div class="wrap">
      <div class="dl-card">
        <div class="section-head" style="margin-bottom:0">
          <p class="eyebrow">Free Download</p>
          <h2>Get the {title} as a PDF</h2>
          <p>The full guide in a printable PDF to keep, share or read offline. Tell me where to send updates and it downloads right away.</p>
        </div>
        <form class="form light" name="guide-download" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-success="Your guide is ready." data-download="{{{{pdf:{file}}}}}" novalidate>
          <input type="hidden" name="form-name" value="guide-download">
          <input type="hidden" name="guide" value="{title}">
          <input type="hidden" name="page" value="{slug}">
          <p hidden><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
          <div class="row">
            <label for="d-name">Name
              <input id="d-name" name="name" autocomplete="name" required>
            </label>
            <label for="d-email">Email
              <input id="d-email" name="email" type="email" autocomplete="email" required>
            </label>
          </div>
          <button class="btn btn-primary" type="submit">Download the PDF</button>
          <p class="consent">By downloading, you agree Chris Nowakiwsky of RE/MAX Professionals may follow up by email. No spam, and you can opt out anytime.</p>
          <p class="form-status" role="status"></p>
        </form>
      </div>
    </div>
  </section>'''


FORM_JS = '''<script>
(function () {
  var LIVE = %s;
  document.querySelectorAll('form[data-netlify]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      if (!form.checkValidity()) {
        status.textContent = 'Please fill in the required fields with a valid email.';
        if (form.reportValidity) form.reportValidity();
        return;
      }
      if (!LIVE) {
        status.textContent = 'Preview only. At launch, this form sends your request straight to Chris.';
        return;
      }
      var button = form.querySelector('button[type="submit"]');
      button.disabled = true;
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        form.reset();
        status.textContent = form.getAttribute('data-success') || 'Thanks. Chris will be in touch within one business day.';
        var file = form.getAttribute('data-download');
        if (file) {
          var link = document.createElement('a');
          link.href = file; link.className = 'btn btn-primary'; link.textContent = 'Open the PDF';
          link.setAttribute('download', '');
          status.appendChild(document.createTextNode(' '));
          status.appendChild(link);
          window.location.href = file;
        }
      }).catch(function () {
        status.textContent = "That didn't go through. Please call or text Chris at (970) 485-2228.";
      }).then(function () { button.disabled = false; });
    });
  });
})();
</script>'''


def parse(page):
    raw = page.read_text()
    m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", raw, re.S)
    if not m:
        raise SystemExit(f"{page.name}: missing <!--meta {{...}} --> block")
    meta = json.loads(m.group(1))
    meta["slug"] = page.stem
    return meta, raw[m.end():]


def text_of(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def schema(meta, body):
    slug = meta["slug"]
    url = DOMAIN + ("/" if slug == "index" else f"/{slug}/")
    graph = [AGENT, PERSON]
    if meta.get("type") == "article":
        graph.append({
            "@type": "Article",
            "headline": meta.get("headline", meta["title"]),
            "description": meta["description"],
            "author": {"@id": PERSON["@id"]},
            "publisher": {"@id": AGENT_ID},
            "datePublished": meta.get("published", meta.get("updated", TODAY)),
            "dateModified": meta.get("updated", TODAY),
            "mainEntityOfPage": url,
            "image": DOMAIN + "/assets/chris-portrait.jpg",
            **({"about": {"@type": "Place", "name": meta["place"]}} if meta.get("place") else {}),
        })
    crumbs = meta.get("crumbs")
    if crumbs:
        items = []
        for i, (name, target) in enumerate(crumbs, 1):
            item = {"@type": "ListItem", "position": i, "name": name}
            if target is not None:
                item["item"] = DOMAIN + ("/" if target == "index" else f"/{target}/")
            items.append(item)
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    faqs = re.findall(r"<details[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>", body, re.S)
    if faqs and meta.get("faq", True):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": text_of(q),
                 "acceptedAnswer": {"@type": "Answer", "text": text_of(a)}}
                for q, a in faqs
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)


def render(meta, body, mode):
    slug = meta["slug"]
    live = mode == "dist"

    def link(target):
        if live:
            return "/" if target == "index" else f"/{target}/"
        return f"{target}.html"

    def asset(name):
        return f"/assets/{name}" if live else f"assets/{name}"

    canonical = DOMAIN + ("/" if slug == "index" else f"/{slug}/")
    flag = "" if live else f'<div class="preview-flag">{meta.get("preview_flag", "Design preview · forms are inactive until launch")}</div>\n'
    content = body
    if meta.get("valuation") is not False:
        content = content.replace("{{valuation}}", valuation(slug, meta.get("valuation", {}) or {}))
    content = content.replace("{{contact}}", contact(slug, meta.get("contact", {}) or {}))
    if meta.get("pdf"):
        content = content.replace("{{download}}", guide_download(slug, meta["pdf"]))
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{meta["title"]}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{html.escape(meta["description"])}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{"article" if meta.get("type") == "article" else "website"}">
<meta property="og:site_name" content="Find Homes Around Denver">
<meta property="og:title" content="{html.escape(meta.get("headline", meta["title"]))}">
<meta property="og:description" content="{html.escape(meta["description"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/chris-portrait.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{{{{asset:../styles.css}}}}">
<script type="application/ld+json">
{schema(meta, body)}
</script>
</head>
<body>
{flag}{header(meta.get("nav"))}

<main>
{content}
</main>

{footer(meta.get("legal_extra", ""))}

{FORM_JS % ("true" if live else "false")}
{meta.get("script", "")}
</body>
</html>
'''
    page = page.replace("{{asset:../styles.css}}", "/styles.css" if live else "styles.css")
    page = re.sub(r"\{\{pdf:([^}]+)\}\}", lambda m: f"/guides/{m.group(1)}" if live else f"guides/{m.group(1)}", page)
    page = re.sub(r"\{\{link:([a-z0-9-]+)\}\}", lambda m: link(m.group(1)), page)
    page = re.sub(r"\{\{asset:([^}]+)\}\}", lambda m: asset(m.group(1)), page)
    leftovers = re.findall(r"\{\{[^}]*\}\}", page)
    if leftovers:
        raise SystemExit(f"{slug}: unresolved placeholders {leftovers}")
    return page


def strip_for_artifact(page):
    """The artifact host wraps its main page in its own document skeleton."""
    page = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", page)
    page = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', "", page)
    page = page.replace("</head>\n<body>\n", "\n")
    page = re.sub(r"</body>\s*</html>\s*$", "", page)
    return page


def main():
    pages = [parse(p) for p in sorted(SRC.glob("*.html"))]
    scripts_dir = ROOT / "src" / "scripts"
    for meta, _ in pages:
        if meta.get("script_file"):
            meta["script"] = "<script>\n" + (scripts_dir / meta["script_file"]).read_text() + "\n</script>"

    # preview, flat files in the site root
    for meta, body in pages:
        out = render(meta, body, "preview")
        if meta["slug"] == "index":
            out = strip_for_artifact(out)
        (ROOT / f'{meta["slug"]}.html').write_text(out)

    # live site
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for meta, body in pages:
        target = DIST / "index.html" if meta["slug"] == "index" else DIST / meta["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(meta, body, "dist"))
    shutil.copy(ROOT / "styles.css", DIST / "styles.css")
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("_*"))
    urls = "".join(
        f"  <url><loc>{DOMAIN}{'/' if m['slug'] == 'index' else '/' + m['slug'] + '/'}</loc><lastmod>{m.get('updated', TODAY)}</lastmod></url>\n"
        for m, _ in pages if not m.get("noindex"))
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    # Files that must sit at the site root as-is (search engine verification, etc.).
    for f in (ROOT / "static").glob("*"):
        shutil.copy(f, DIST / f.name)
    (DIST / "_redirects").write_text(
        "https://wonderful-phoenix-3e897c.netlify.app/* https://findhomesarounddenver.com/:splat 301!\n"
        "http://wonderful-phoenix-3e897c.netlify.app/* https://findhomesarounddenver.com/:splat 301!\n")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"built {len(pages)} pages:", ", ".join(m["slug"] for m, _ in pages))
    # PDFs live in dist/, which is rebuilt above, so regenerate them every time.
    import subprocess, sys
    subprocess.run([sys.executable, str(ROOT / "src" / "make_pdfs.py")], check=True)


if __name__ == "__main__":
    main()
