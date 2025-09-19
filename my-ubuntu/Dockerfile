FROM python:3.9-slim

WORKDIR /app

RUN useradd myuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown myuser:myuser ./*

USER myuser

EXPOSE 5000

CMD ["python", "app.py"]