## Truthlens — Misinformation Scanner

Dark, neon-accented desktop UI to scan URLs or uploaded media and present a clear verdict with confidence and a concise data summary.

### Scripts
```bash
npm run dev     # start dev server
npm run build   # type-check and build
npm run preview # preview production build
```

### Docker
```bash
docker build -t truthlens:latest .
docker run -p 5173:80 truthlens:latest
```

### CI / Docker Hub
A GitHub Actions workflow is provided at `.github/workflows/docker.yml`.
Add repo secrets:
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN (classic access token)

On pushes to `main`, the image `truthlens:latest` will be built and pushed as `<username>/truthlens:latest`.