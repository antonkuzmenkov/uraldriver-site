# Урал-Драйвер — материалы для ревью (свежий снапшот)

Полная копия репозитория **uraldriver-site** + исходный концепт-документ.
Свежий снапшот после серии правок 5 мая 2026.

🌐 Живой сайт: **https://uraldriver.ru**
📦 Репо: **https://github.com/antonkuzmenkov/uraldriver-site**
🎨 Версия: **v3 — aerospace SPA с космическим фоном**

---

## Что нового с прошлого ревью

### Дизайн (aerospace SPA)
- Чёрный фон `#05070b` + Source Serif для заголовков + JetBrains Mono для меток
- Оранжевый акцент `#ff5b1f`
- Карточки с угловыми маркерами (corner-tl/tr/bl/br)

### Космический фон по секциям главной (вниз — продолжение)
1. Hero — **Земля** + орбита с капсулой
2. Тезисы — **Луна слева** (первый шаг)
3. Прометей-РФ — **Луна справа крупно**
4. Дорожная карта — **Марс**
5. Сценарии загрузки — **Юпитер**
6. Рычаги $/кг — **Туманность**
7. Структура CAPEX — **Юпитер**
8. Матрица Starship — **Нептун**
9. Тех.стек — **Меркурий**
10. 11 глав — **Сатурн с кольцами**
11. Цитата — **Нептун**
12. Журнал — **туманность**

### SVG-визуализации в стиле сайта
- **WaterfallChart** — рычаги $/кг ($230 → $103)
- **CapexChart** — горизонтальные бары структуры $30 млрд
- **StarshipMatrix** — 4×4 heatmap Starship × загрузка

### Интерактивные аккордеоны
- **11 глав** с раскрытием на клик (summary + ссылка на markdown)
- **6 фаз дорожной карты** с целями + gate-review
- **7 рычагов снижения цены** с детальным описанием каждого

### Per-page фоны (через #hash routing)
- /#concept — Земля + орбита
- /#site — гора Народная (UralBackdrop)
- /#economics — Юпитер
- /#roadmap — Марс
- /#phase05 — Луна
- /#competitors — Нептун
- /#blog — туманность
- /#support — спиральная галактика

### Технические детали
- Favicon (SVG + PNG fallback + apple-touch-icon)
- Open Graph метатеги для соцсетей
- HTTPS включён + Let's Encrypt автообновление
- HTTP→HTTPS redirect (https_enforced)
- DNS защита: SPF + DMARC + DKIM-revoked + CAA letsencrypt.org
- ✏️ Имя: Антон **Кузменков** (без мягкого знака)
- 💬 Контакт: **MAX мессенджер** @uraldriver (вместо Telegram)

---

## Что прочитать СНАЧАЛА

**Если есть 5 минут:**
1. Открыть https://uraldriver.ru — пролистать главную, потыкать в фазы и главы
2. Кликнуть в навигации «Прометей-РФ» — самое свежее обновление 2026-05-04

**Если есть 15 минут:**
3. `concept-document/chapters/00_executive_summary.md` — суть проекта
4. `concept-document/chapters/11_prometheus_rf_lab_prototype.md` — Фаза 0.5
5. `concept-document/UPDATES_2026-05-04.md` — журнал последних изменений

**Если есть 1-2 часа:**
6. Все 11 глав по порядку (`concept-document/chapters/`)
7. 4 research-приложения (`concept-document/research/`)

---

## Структура папки

```
UralDriver/
│
├── README_FOR_REVIEWER.md         ← этот файл
├── README.md                      ← README репо (тех.инфо)
│
├── concept-document/              ⭐ ИСХОДНЫЙ КОНЦЕПТ-ДОКУМЕНТ
│   ├── README.md                  ← обзор всех 11 глав
│   ├── chapters/                  ← 11 глав по порядку
│   │   ├── 00_executive_summary.md         (5 мин)
│   │   ├── 01_concept_and_physics.md       (14 мин — физика, MHD)
│   │   ├── 02_site_analysis.md             (12 мин — гора Народная)
│   │   ├── 03_technical_design.md          (22 мин — все системы)
│   │   ├── 04_economics.md                 (24 мин — экономика, Starship)
│   │   ├── 05_synergy_rosatom.md           (11 мин)
│   │   ├── 06_demand_and_market.md         (18 мин — главный риск)
│   │   ├── 07_roadmap.md                   (16 мин — 6 фаз)
│   │   ├── 08_risks.md                     (13 мин)
│   │   ├── 09_alternatives_comparison.md   (20 мин — конкуренты)
│   │   ├── 10_strategy_for_promotion.md    (17 мин)
│   │   └── 11_prometheus_rf_lab_prototype.md ⭐ (28 мин — главное обновление)
│   ├── research/
│   ├── sources.md
│   └── UPDATES_2026-05-04.md
│
├── static/
│   ├── index.html                 ⭐ ВЕСЬ САЙТ В ОДНОМ ФАЙЛЕ
│   │                                (1838+ строк, React 18 SPA через Babel CDN,
│   │                                 inline CSS + JSX в <script type="text/babel">)
│   ├── favicon.svg + ico + PNG    (иконка для вкладки браузера)
│   ├── apple-touch-icon.png       (180×180 для iOS)
│   ├── CNAME                      (uraldriver.ru — для GitHub Pages)
│   └── img/charts/                (исходные PNG из HABR-статьи —
│                                   на сайте сейчас inline SVG, PNG для referenced)
│
├── layouts/_default/              ← Hugo layouts для редиректов на #hash
├── content/                       ← Markdown-страницы (legacy, sites SPA-redirect)
├── config/_default/hugo.toml      ← Hugo конфиг
└── .github/workflows/deploy.yml   ← CI/CD
```

---

## Главное для дизайн-ревью

Файл всё ещё один — **`static/index.html`** (~162 KB). Структурирован так:
1. **CSS** в `<style>` (строки ~10-1000) — все правила в одном блоке, секциями
2. **`window.SITE_DATA`** в `<script>` (строки ~1000-1300) — весь контент сайта
3. **JSX-компоненты** в нескольких `<script type="text/babel">` блоках:
   - `components.jsx` — иконки, Frame, Btn, Tag, Stat, SectionHead
   - `lab.jsx` — Backdrop'ы (планеты), ChaptersAccordion, LeversAccordion, графики
   - `chrome.jsx` — Nav, Footer, ScrollProgress
   - `pages-home.jsx` — главная
   - `pages-inner.jsx` — внутренние страницы
   - `app.jsx` — App + routing

## Главные вопросы для ревью

1. **Контент-плотность** — много ли «воды»? Где можно сократить?
2. **Графики** — понятно ли с первого взгляда? Что бы добавил?
3. **Аккордеоны** — 11 глав / 6 фаз / 7 рычагов раскрываются. Удобно или перегружено?
4. **Космический фон** — не отвлекает ли от чтения? Контраст ОК?
5. **Honest score** — где видны слабости проекта? Хорошо ли они признаны?
6. **Customer-mix** (Глава 6) — реалистичен ли встроенный customer?
7. **Starship-чувствительность** (Глава 4.5) — корректны ли вероятности S2=50% / S3=25%?
8. **Прометей-РФ финансирование** — реалистичен ли mix-канал (МО + РНФ + in-kind + Сколково + крауд)?

---

## Контакты автора

**Антон Кузменков**
- MAX мессенджер: @uraldriver
- Email: anton@moyvedi.ru
- GitHub: https://github.com/antonkuzmenkov

---

*Снапшот: 2026-05-05 16:12 MSK · v3 aerospace SPA*
