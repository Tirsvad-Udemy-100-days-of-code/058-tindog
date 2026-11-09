[English](Running-the-Project) · **Dansk** · [Bahasa Malaysia](Running-the-Project-ms)

# Sådan kører du projektet

## Krav

- Python 3.13 eller nyere
- En webbrowser med internetadgang (Bootstrap hentes fra et CDN)

## Opsætning

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Linux og macOS bruges `python3 -m venv .venv` og `source .venv/bin/activate`.

## Server siderne

```bash
python -m tindog
```

Åbn `http://127.0.0.1:8058/` i en browser. Brug `--host` og `--port` til at ændre adressen.

## Kør testene

```bash
python -m pytest
```

## Tag skærmbillederne

Skærmbillederne i denne wiki er taget i en Docker-container, så skrivebordet ikke bruges:

```bash
docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
docker run --rm -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
```
