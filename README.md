# Data Engineering Roadmap 2026–2027

Interactive, browser-based roadmap for learning modern data engineering. The application includes a structured checklist, curated resources, an animated production pipeline, notes, and guided SQL/Python practice.

## Live site

[data-engineering-workbook.vercel.app](https://data-engineering-workbook.vercel.app)

## Project structure

```text
.
├── index.html              # Complete static web application
├── README.md               # Project overview and local setup
├── .gitignore              # Local and sensitive files excluded from Git
└── docs/
    └── DEPLOYMENT.md       # Deployment and release instructions
```

The application intentionally remains self-contained in `index.html`. Its styles, data, and runtime logic are inline so the roadmap can be deployed as a static site without a build step.

## Run locally

From the project directory:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

Stop the server with `Ctrl + C`.

## Development workflow

- `main` contains the public production version.
- `develop` is used for local changes and review.
- Verify changes locally before merging `develop` into `main`.
- Do not commit `.vercel/`, environment files, editor settings, or generated logs.

## Persistence

Checklist progress and notes are stored in each visitor’s browser. Users do not share progress with one another.

## Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
