// Cash to close: down payment + closing costs + inspections - seller credits - assistance.
function cashToClose(i) {
  var down = i.price * i.downPct / 100;
  var closing = i.price * i.closingPct / 100;
  // Seller credits can only offset closing costs, never the down payment.
  var credit = Math.min(i.credit, closing);
  var total = Math.max(0, down + closing + i.inspect - credit - i.dpa);
  return { down: down, closing: closing, credit: credit, total: total };
}

(function () {
  var root = document.getElementById('ctc-calc');
  if (!root) return;
  var $ = function (id) { return document.getElementById(id); };
  var money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  var num = function (id) { var v = parseFloat($(id).value); return isFinite(v) && v > 0 ? v : 0; };

  function update() {
    var r = cashToClose({
      price: num('ctc-price'), downPct: Math.min(num('ctc-down'), 100), closingPct: num('ctc-closing'),
      inspect: num('ctc-inspect'), credit: num('ctc-credit'), dpa: num('ctc-dpa')
    });
    $('ctc-total').textContent = money.format(r.total);
    $('ctc-sub').textContent = 'to buy this home, plus whatever savings you want to keep as a cushion.';
    $('ctc-o-down').textContent = money.format(r.down);
    $('ctc-o-closing').textContent = money.format(r.closing);
    $('ctc-o-inspect').textContent = money.format(num('ctc-inspect'));
    $('ctc-o-credit').textContent = '−' + money.format(r.credit);
    $('ctc-o-dpa').textContent = '−' + money.format(num('ctc-dpa'));
  }

  root.addEventListener('input', update);
  root.addEventListener('change', update);
  update();
})();
