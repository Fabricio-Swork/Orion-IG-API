@echo off
call venv\Scripts\activate
echo Iniciando servidor Uvicorn...
uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --workers 1 --lifespan off
pause
