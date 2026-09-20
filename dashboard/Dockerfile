FROM python:3.11-slim

WORKDIR /app

COPY app.py index.html ./

EXPOSE 9120

ENV DASHBOARD_HOST=0.0.0.0
ENV DASHBOARD_PORT=9120

CMD ["python", "app.py"]
