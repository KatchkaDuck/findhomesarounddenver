// Seller net proceeds estimate.
function sellerNet(i) {
  var brokerage = i.price * i.feePct / 100;
  // Colorado taxes are paid in arrears; the seller credits Jan 1 through the closing date.
  var taxCredit = i.annualTax * (i.dayOfYear / 365);
  var other = i.concessions + i.hoa;
  var costs = brokerage + i.title + taxCredit + other;
  return {
    brokerage: brokerage,
    title: i.title,
    taxCredit: taxCredit,
    other: other,
    costs: costs,
    costPct: i.price > 0 ? costs / i.price * 100 : 0,
    net: i.price - i.payoff - costs
  };
}

(function () {
  var root = document.getElementById('net-calc');
  if (!root) return;
  var $ = function (id) { return document.getElementById(id); };
  var money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  var num = function (id) { var v = parseFloat($(id).value); return isFinite(v) && v > 0 ? v : 0; };

  // Default closing month: next month, the usual 30 to 45 days out.
  $('nc-month').value = String((new Date().getMonth() + 1) % 12);

  // Fields with data-auto follow the sale price until someone edits them.
  var autoFields = root.querySelectorAll('[data-auto]');
  autoFields.forEach(function (f) { f.addEventListener('input', function () { f.dataset.edited = '1'; }); });

  function midMonthDay(m) {
    var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var d = 15;
    for (var k = 0; k < m; k++) d += days[k];
    return d;
  }

  function update() {
    var price = num('nc-price');
    autoFields.forEach(function (f) {
      if (!f.dataset.edited) f.value = Math.round(price * parseFloat(f.dataset.auto) / 50) * 50;
    });
    var r = sellerNet({
      price: price,
      payoff: num('nc-payoff'),
      feePct: num('nc-fees'),
      title: num('nc-title'),
      annualTax: num('nc-tax'),
      dayOfYear: midMonthDay(parseInt($('nc-month').value, 10)),
      concessions: num('nc-concessions'),
      hoa: num('nc-hoa')
    });
    $('nc-net').textContent = money.format(r.net);
    $('nc-sub').textContent = 'after paying off your loan. Selling costs come to about ' +
      money.format(r.costs) + ', or ' + r.costPct.toFixed(1) + '% of the price.';
    $('nc-o-price').textContent = money.format(price);
    $('nc-o-brokerage').textContent = '−' + money.format(r.brokerage);
    $('nc-o-title').textContent = '−' + money.format(r.title);
    $('nc-o-tax').textContent = '−' + money.format(r.taxCredit);
    $('nc-o-other').textContent = '−' + money.format(r.other);
    $('nc-o-payoff').textContent = '−' + money.format(num('nc-payoff'));
  }

  root.addEventListener('input', update);
  root.addEventListener('change', update);
  update();
})();
