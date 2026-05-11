---
title: "Калькулятор экономики"
description: "Интерактивная модель удельной стоимости пуска. Подвигай ползунки и посмотри, как меняется $/кг при разном CAPEX, темпе пусков и операционных расходах."
weight: 35
date: 2026-05-11
---

> Простая модель удельной стоимости вывода 1 кг полезной нагрузки на орбиту через УД. Базовые числа взяты из главы [/economics/](/economics/). Подвигай ползунки — увидишь, как объём рынка ломает цену.

<div id="ud-calc">
  <div class="ud-calc-row">
    <label>CAPEX капитальные затраты, $ млрд: <output id="capex-out">30</output></label>
    <input type="range" id="capex" min="20" max="50" step="1" value="30">
  </div>
  <div class="ud-calc-row">
    <label>Темп пусков в год: <output id="rate-out">500</output></label>
    <input type="range" id="rate" min="100" max="2000" step="50" value="500">
  </div>
  <div class="ud-calc-row">
    <label>Полезная нагрузка на капсулу, т: <output id="pn-out">1.0</output></label>
    <input type="range" id="pn" min="0.5" max="2.0" step="0.1" value="1.0">
  </div>
  <div class="ud-calc-row">
    <label>OPEX операционные расходы, $ млн/год: <output id="opex-out">370</output></label>
    <input type="range" id="opex" min="200" max="700" step="10" value="370">
  </div>
  <div class="ud-calc-row">
    <label>Срок амортизации, лет: <output id="years-out">30</output></label>
    <input type="range" id="years" min="15" max="50" step="1" value="30">
  </div>

  <div class="ud-calc-result">
    <div class="ud-calc-big">
      <span class="ud-calc-label">$/кг ПОЛНАЯ</span>
      <span class="ud-calc-value" id="full-out">$3 700</span>
    </div>
    <div class="ud-calc-big">
      <span class="ud-calc-label">$/кг УДЕЛЬНАЯ (OPEX/ПН)</span>
      <span class="ud-calc-value" id="marg-out">$740</span>
    </div>
  </div>

  <div class="ud-calc-context" id="context"></div>
</div>

<style>
#ud-calc {
  margin: 30px 0;
  padding: 24px;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--frame-2);
  border-radius: 6px;
}
.ud-calc-row { margin-bottom: 18px; }
.ud-calc-row label {
  display: flex;
  justify-content: space-between;
  font-family: "SF Mono", Menlo, monospace;
  font-size: 13px;
  color: var(--ink-2);
  margin-bottom: 6px;
}
.ud-calc-row output { color: var(--accent); font-weight: 600; }
.ud-calc-row input[type=range] {
  width: 100%;
  accent-color: var(--accent);
}
.ud-calc-result {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
  margin-top: 28px;
  padding: 22px;
  background: rgba(13,21,37,0.6);
  border-radius: 4px;
  border: 1px solid var(--frame);
}
@media (max-width: 600px) { .ud-calc-result { grid-template-columns: 1fr; } }
.ud-calc-big {
  display: flex; flex-direction: column;
  align-items: center;
}
.ud-calc-label {
  font-size: 11px;
  letter-spacing: 1.2px;
  color: var(--dim);
  text-transform: uppercase;
  font-family: "SF Mono", monospace;
}
.ud-calc-value {
  font-size: 42px;
  font-weight: 700;
  color: var(--accent);
  margin-top: 8px;
  font-family: "SF Mono", Menlo, monospace;
}
.ud-calc-context {
  margin-top: 24px;
  padding: 16px 18px;
  background: rgba(78,195,212,0.05);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--ink-2);
}
.ud-calc-context strong { color: var(--ink); }
</style>

<script>
(function() {
  const inputs = {
    capex: document.getElementById('capex'),
    rate: document.getElementById('rate'),
    pn: document.getElementById('pn'),
    opex: document.getElementById('opex'),
    years: document.getElementById('years'),
  };
  const outs = {
    capex: document.getElementById('capex-out'),
    rate: document.getElementById('rate-out'),
    pn: document.getElementById('pn-out'),
    opex: document.getElementById('opex-out'),
    years: document.getElementById('years-out'),
    full: document.getElementById('full-out'),
    marg: document.getElementById('marg-out'),
  };
  const ctx = document.getElementById('context');

  function fmt(n) { return Math.round(n).toLocaleString('ru-RU').replace(/,/g, ' '); }

  function recalc() {
    const capex = +inputs.capex.value;
    const rate = +inputs.rate.value;
    const pn = +inputs.pn.value;
    const opex = +inputs.opex.value;
    const years = +inputs.years.value;

    outs.capex.textContent = capex;
    outs.rate.textContent = rate;
    outs.pn.textContent = pn.toFixed(1);
    outs.opex.textContent = opex;
    outs.years.textContent = years;

    const totalPN_tons = rate * pn;
    const totalPN_kg = totalPN_tons * 1000;

    const capexPerYear_M = (capex * 1000) / years;
    const totalCost_M_per_year = capexPerYear_M + opex;

    const fullCostPerKg = totalCost_M_per_year * 1e6 / totalPN_kg;
    const marginalCostPerKg = opex * 1e6 / totalPN_kg;

    outs.full.textContent = '$' + fmt(fullCostPerKg);
    outs.marg.textContent = '$' + fmt(marginalCostPerKg);

    let verdict = '';
    if (marginalCostPerKg < 200) {
      verdict = `<strong>Сценарий А — конкурентен Starship.</strong> При ${rate} пусков/год и $${opex}М OPEX удельная стоимость $${fmt(marginalCostPerKg)}/кг пробивает целевую Starship $100-200/кг. Это режим максимального государственного спроса (Cislunar economy раскрылся к 2045+).`;
    } else if (marginalCostPerKg < 500) {
      verdict = `<strong>Сценарий Б — базовый v3.2.</strong> Удельная стоимость $${fmt(marginalCostPerKg)}/кг — реалистичный режим для массового топлива и металлов к околунному депо. УД и Starship — на разных рынках, не конкуренты.`;
    } else if (marginalCostPerKg < 1000) {
      verdict = `<strong>Сценарий В — минимум суверенитета.</strong> $${fmt(marginalCostPerKg)}/кг удельная — пользы для геополитической независимости больше, чем для коммерции. Окупаемость 30-50 лет, как у БАМ и Севморпути.`;
    } else {
      verdict = `<strong>Сценарий Г — «памятник».</strong> $${fmt(marginalCostPerKg)}/кг — спрос не материализовался, программа работает в минимальном режиме. Это риск 25-35% в Карте рисков v3.2.`;
    }

    ctx.innerHTML = `Полная стоимость <strong>$${fmt(fullCostPerKg)}/кг</strong> учитывает амортизацию $${capex} млрд CAPEX за ${years} лет. Удельная <strong>$${fmt(marginalCostPerKg)}/кг</strong> — только следующий пуск без капитальных затрат (то, что коммерчески важно для конкуренции).<br><br>${verdict}<br><br>Подробнее в <a href="/economics/" style="color:var(--accent)">главе экономики</a> и <a href="/competitors/" style="color:var(--accent)">сравнении с конкурентами</a>.`;
  }

  Object.values(inputs).forEach(i => i.addEventListener('input', recalc));
  recalc();
})();
</script>

## Как это работает

**Полная стоимость** = (CAPEX/срок_амортизации + OPEX) / (пусков_в_год × ПН_кг).

**Удельная стоимость** = OPEX / (пусков_в_год × ПН_кг). Без учёта капитальных затрат — это «следующий пуск», то что коммерчески важно для конкуренции со Starship.

## Базовый сценарий v3.2

- **CAPEX**: $30 млрд за 15 лет программы 2030-2045 (тоннель, магниты, ВВЭР, импульсная энергетика, капсулы)
- **OPEX**: $370 млн/год (электричество $150М + персонал $50М + амортизация капсул $80М + расходники + страховка)
- **Темп**: 500-1000 пусков/год при выходе в рабочий режим
- **ПН**: 1 т из 20 т стартовой массы (массовая доля 5%, как у обычной ракеты)
- **Амортизация**: 30 лет — стандартный срок для государственной инфраструктуры

Базовый сценарий Б даёт удельную **$300-500/кг**. Это **в 3-10 раз дороже** целевой Starship $100-200/кг — и в этом не дефект, а другая ниша: УД — стратегическая инфраструктура для bulk-грузов на полярные орбиты, не коммерческая ракета.

[Полный анализ — на /economics/](/economics/).
