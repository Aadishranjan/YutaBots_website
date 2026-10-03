FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY main.py index.html ./

EXPOSE 8000
CMD ["python", "main.py"]
