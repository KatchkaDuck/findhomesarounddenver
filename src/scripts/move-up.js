// Move-up budget: how much purchase price your equity supports as a down payment.
function moveUpBudget(i) {
  var equity = i.value * (1 - i.costPct / 100) - i.payoff;
  var down = Math.max(0, equity + i.savings - i.reserve);
  var maxPrice = i.downPct > 0 ? down / (i.downPct / 100) : 0;
  return { equity: equity, down: down, maxPrice: maxPrice, loan: Math.max(0, maxPrice - down) };
}

(function () {
  var root = document.getElementById('moveup-calc');
  if (!root) return;
  var $ = function (id) { return document.getElementById(id); };
  var money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  var num = function (id) { var v = parseFloat($(id).value); return isFinite(v) && v > 0 ? v : 0; };

  function update() {
    var downPct = parseFloat($('mu-down').value);
    var r = moveUpBudget({
      value: num('mu-value'), payoff: num('mu-payoff'), costPct: num('mu-cost'),
      savings: num('mu-savings'), reserve: num('mu-reserve'), downPct: downPct
    });
    // Round the headline down to the nearest $5,000 so it never overstates.
    $('mu-max').textContent = money.format(Math.floor(r.maxPrice / 5000) * 5000);
    $('mu-sub').textContent = 'with ' + downPct + '% down, a down payment of ' + money.format(r.down) + '.';
    $('mu-o-equity').textContent = money.format(r.equity);
    $('mu-o-savings').textContent = '+' + money.format(num('mu-savings'));
    $('mu-o-reserve').textContent = '−' + money.format(num('mu-reserve'));
    $('mu-o-down').textContent = money.format(r.down);
    $('mu-o-loan').textContent = money.format(r.loan);
  }

  root.addEventListener('input', update);
  root.addEventListener('change', update);
  update();
})();
