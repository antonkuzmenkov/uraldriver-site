# uraldriver-site

Сайт проекта **«Урал-Драйвер»** — концепта подземной электромагнитной катапульты на Приполярном Урале.

🌐 https://uraldriver.ru

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
