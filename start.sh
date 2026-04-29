gunicorn -w 4 -k uvicorn.workers.UvicornWorker titanium_v4_core:app
