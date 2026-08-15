# Data Engineering Roadmap 2026–2027

An interactive roadmap for understanding the skills, systems, and practices required in modern data engineering.

## Explore the roadmap

**[Open the live application](https://data-engineering-workbook.vercel.app)**

## What it includes

- A structured learning path from business requirements and foundations to production architecture.
- SQL, Python, data modeling, ingestion, storage, transformation, orchestration, governance, and observability topics.
- An animated end-to-end production pipeline showing how data moves from sources to business consumption.
- Curated documentation, courses, books, and technical references for every major section.
- A guided PostgreSQL practice workspace for applying SQL concepts.
- Personal notes and checklist progress stored privately in each visitor’s browser.

## How progress works

The application does not require an account. Checklist progress and notes remain in the visitor’s browser and are not shared with other users.

## Technology

The roadmap is a self-contained static web application:

- HTML, CSS, and JavaScript
- Tailwind CSS
- Lucide icons
- PGlite for browser-based PostgreSQL practice
- Vercel for hosting

No application server or build process is required to serve the roadmap.

## Repository structure

```text
.
├── index.html
├── README.md
├── .gitignore
└── docs/
    └── DEPLOYMENT.md
```

Deployment and release procedures are documented in [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

## Project status

The public version is maintained on `main`. Changes are reviewed on `develop` before production release.
