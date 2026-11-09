**English** · [Dansk](Running-the-Project-da) · [Bahasa Malaysia](Running-the-Project-ms)

# Running the project

## Requirements

- Python 3.13 or newer
- A web browser with internet access (Bootstrap is loaded from a CDN)

## Set up

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Linux and macOS use `python3 -m venv .venv` and `source .venv/bin/activate`.

## Serve the pages

```bash
python -m tindog
```

Open `http://127.0.0.1:8058/` in a browser. Use `--host` and `--port` to change the address.

## Run the tests

```bash
python -m pytest
```

## Take the screenshots

The screenshots in this wiki are taken in a Docker container, so the desktop is not used:

```bash
docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
docker run --rm -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
```
