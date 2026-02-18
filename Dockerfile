# Python 3.11 slim image
FROM python:3.11-slim

# Munka könyvtár
WORKDIR /app

# Függőségek telepítése
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App fájlok másolása
COPY . .

# Port beállítás
ENV PORT=10000

# Start gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
