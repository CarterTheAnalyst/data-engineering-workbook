# Deployment guide

The roadmap is a static site deployed to Vercel. It does not require a build command or server runtime.

## Environments

- **Local:** `http://localhost:8000`
- **Development:** branch `develop`
- **Production:** branch `main`
- **Public URL:** [https://data-engineering-workbook.vercel.app](https://data-engineering-workbook.vercel.app)

## Local verification

Run the site from the repository root:

```bash
python3 -m http.server 8000
```

Open the local URL and verify:

1. The roadmap loads without visible errors.
2. Sections expand and collapse correctly.
3. Checklist progress persists after refresh.
4. The animated pipeline renders and responds to its controls.
5. SQL and Python practice interfaces load.
6. Resource links open correctly.
7. Desktop and mobile layouts remain usable.

## Release workflow

```bash
git switch develop
git status
git push origin develop
```

After validation, merge `develop` into `main` and push `main`. The production deployment should only use a reviewed `main` commit.

## Manual Vercel deployment

If Git-based deployment is unavailable:

```bash
npx vercel --prod
```

The local `.vercel/` directory contains machine-specific project linkage and must remain excluded from Git.

## Rollback

If a production release fails, use the Vercel dashboard to promote the last known-good deployment, or revert the problematic Git commit and push `main` again.
