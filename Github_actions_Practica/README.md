# StockGuard - Practica de GitHub Actions

Practica de CI con Python, pytest y Pull Requests (Big Data - Ingenieria de Sistemas).
Actividad preparatoria para el Proyecto Final RapidGo 360.

## Regla de negocio

| Condicion | Resultado |
|---|---|
| stock actual = 0 | AGOTADO |
| stock actual <= 50 % del stock minimo | CRITICO |
| stock actual <= stock minimo | BAJO |
| otro caso | NORMAL |
| stock negativo o minimo <= 0 | ValueError |

## Ejecutar localmente

```bash
python -m pip install -r requirements.txt
pytest -v
```

## CI

El workflow `.github/workflows/ci.yml` se ejecuta en:
- `push` a `main`
- `pull_request` hacia `main`
- ejecucion manual (`workflow_dispatch`)

Pasos: checkout -> Python 3.12 -> instalar dependencias -> compileall -> pytest.
