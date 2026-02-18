# 1. Alap Python image
FROM python:3.11-slim

# 2. Munkakönyvtár
WORKDIR /app

# 3. Függőségek
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. A teljes app másolása
COPY . .

# 5. Port
EXPOSE 10000

# 6. Gunicorn parancs
CMD ["gunicorn", "--chdir", "/app", "wsgi:app", "--bind", "0.0.0.0:10000", "--workers", "1"]
