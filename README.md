

This repository contains a small web application. It currently includes:

- `app.py` — application entry (Flask for local dev)
- `templates/index.html` — example template

How to run locally (Flask):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # or: pip install flask
python3 app.py
# then open http://127.0.0.1:5000
```

If you want to deploy to Azure, see the project root for suggested `Dockerfile` and `requirements.txt` options.
