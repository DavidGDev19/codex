# Cyber Dashboard

Dashboard corporativo de ciberseguridad.

## Puesta en marcha

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
./scripts/build-css.ps1
$env:FLASK_ENV='development'
python backend/app.py
```

Pruebas básicas:

```bash
curl http://localhost:5000/api/noticias
```

