[English](Running-the-Project) · [Dansk](Running-the-Project-da) · **Bahasa Malaysia**

# Cara menjalankan projek

## Keperluan

- Python 3.13 atau lebih baharu
- Pelayar web dengan capaian internet (Bootstrap dimuatkan daripada CDN)

## Penyediaan

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Pada Linux dan macOS gunakan `python3 -m venv .venv` dan `source .venv/bin/activate`.

## Sajikan halaman

```bash
python -m tindog
```

Buka `http://127.0.0.1:8058/` dalam pelayar. Gunakan `--host` dan `--port` untuk menukar alamat.

## Jalankan ujian

```bash
python -m pytest
```

## Ambil tangkapan skrin

Tangkapan skrin dalam wiki ini diambil dalam bekas Docker, supaya desktop tidak digunakan:

```bash
docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
docker run --rm -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
```
