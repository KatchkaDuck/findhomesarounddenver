// Monthly payment estimate: principal and interest, taxes, insurance, mortgage insurance, HOA.
function monthlyPayment(i) {
  var loan = i.price * (1 - i.downPct / 100);
  var n = i.years * 12;
  var r = i.ratePct / 100 / 12;
  var pi = loan <= 0 ? 0 : (r === 0 ? loan / n : loan * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1));
  var pmi = i.downPct < 20 ? loan * 0.005 / 12 : 0;
  var tax = i.annualTax / 12, ins = i.annualIns / 12;
  return { loan: loan, pi: pi, tax: tax, ins: ins, pmi: pmi, hoa: i.hoa, total: pi + tax + ins + pmi + i.hoa };
}

(function () {
  var root = document.getElementById('pay-calc');
  if (!root) return;
  var $ = function (id) { return document.getElementById(id); };
  var money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  var num = function (id) { var v = parseFloat($(id).value); return isFinite(v) && v > 0 ? v : 0; };
  var autoFields = root.querySelectorAll('[data-auto]');
  autoFields.forEach(function (f) { f.addEventListener('input', function () { f.dataset.edited = '1'; }); });

  function update() {
    var price = num('pc-price');
    autoFields.forEach(function (f) {
      if (!f.dataset.edited) f.value = Math.round(price * parseFloat(f.dataset.auto) / 50) * 50;
    });
    var r = monthlyPayment({
      price: price, downPct: Math.min(num('pc-down'), 100), ratePct: num('pc-rate'),
      years: parseInt($('pc-term').value, 10), annualTax: num('pc-tax'), annualIns: num('pc-ins'), hoa: num('pc-hoa')
    });
    $('pc-total').textContent = money.format(r.total);
    $('pc-sub').textContent = 'per month. At about 30% of gross income, that fits a household earning around ' +
      money.format(Math.ceil(r.total * 12 / 0.3 / 1000) * 1000) + ' a year.';
    $('pc-o-pi').textContent = money.format(r.pi);
    $('pc-o-tax').textContent = money.format(r.tax);
    $('pc-o-ins').textContent = money.format(r.ins);
    $('pc-o-pmi').textContent = money.format(r.pmi);
    $('pc-o-hoa').textContent = money.format(r.hoa);
    $('pc-o-loan').textContent = money.format(r.loan);
  }

  root.addEventListener('input', update);
  root.addEventListener('change', update);
  update();
})();
