# uraldriver-site

Сайт + концепт-документ проекта **«Урал-Драйвер»** — подземной электромагнитной катапульты на Приполярном Урале.

🌐 https://uraldriver.ru
📄 Версия концепта: **v3.2** (после критики на [Хабре](https://habr.com/ru/articles/1033192/))

> Версия v3.2 (9 мая 2026) переработана после 600+ комментариев на Хабре. Главные изменения: скорость в тоннеле 6,5 → 2,5 км/с (Mach 7,3) при 8 g sustained, MHD plasma window заменён на He buffer + кевларовая мембрана + Fast-Acting Valve, добавлена бортовая ГПВРД-ступень, marginal cost $300–500/кг для bulk propellant, позиционирование сменилось с «конкурент Starship» на «стратегическая инфраструктура РФ» (аналог БАМ, ITER, СМП). Подробности — в [главе 12 концепт-документа](concept-document/chapters/12_v3_2_pivot.md).

## Содержимое репозитория

- **`content/`** — Markdown-страницы сайта (адаптированные для Hugo + Blowfish);
- **`concept-document/`** — полный исходный концепт-документ из 11 глав + research-приложения;
- **`layouts/`** — кастомная главная страница (визионерский лендинг);
- **`config/`** — конфигурация Hugo (тема, меню, локализация RU);
- **`.github/workflows/deploy.yml`** — автодеплой на GitHub Pages.

## Стек

- [Hugo](https://gohugo.io) v0.161.1+ (static site generator)
- [Blowfish](https://blowfish.page) theme (Tailwind CSS, dark mode)
- GitHub Pages (хостинг)
- GitHub Actions (CI/CD)

## Структура

```
content/
├── _index.md              # Главная (custom layout)
├── concept/               # Концепция и физика
├── site/                  # Площадка (гора Народная)
├── technical/             # Техническое решение
├── economics/             # Экономика
├── synergy/               # Синергия с Росатомом
├── roadmap/               # Дорожная карта
├── phases/
│   ├── phase-0/           # Концепт
│   ├── phase-05/          # ⭐ Прометей-РФ (главное обновление 2026-05-04)
│   ├── phase-1/           # Демонстратор
│   ├── phase-2/           # Стройка
│   ├── phase-3/           # ЛКИ
│   └── phase-4/           # Эксплуатация
├── option-b/              # Лунный масс-драйвер
├── competitors/           # Конкурентный ландшафт 2026
├── risks/                 # Риски и митигация
├── promotion/             # Стратегия продвижения
├── blog/                  # Журнал проекта
├── support/               # Поддержать проект
├── about/                 # Об авторе
├── contact/               # Контакты
└── changelog/             # История изменений
```

## Локальная разработка

```bash
git clone --recursive https://github.com/antonkuzmenkov/uraldriver-site.git
cd uraldriver-site
hugo server --buildDrafts
# открыть http://localhost:1313
```

## Деплой

Автоматически через GitHub Actions при push в `master`. См. `.github/workflows/deploy.yml`.

## Лицензия

Концепт-документ доступен под Creative Commons BY-SA 4.0. Код сайта (тема, конфиги) — MIT.

## Автор

Антон Кузьменков — [Telegram](https://t.me/uraldriver) — [Email](mailto:anton@moyvedi.ru)
