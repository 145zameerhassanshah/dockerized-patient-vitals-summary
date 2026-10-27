FROM python:3.12-slim

WORKDIR /app

COPY patient_summary.py .
COPY patient_vitals.csv .

CMD ["python", "patient_summary.py"]
