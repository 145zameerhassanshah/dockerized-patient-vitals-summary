# Dockerized Patient Vitals Summary

A Dockerized Python project created during the CMIT AI Internship to learn how to write a Dockerfile, build a custom image, run a container, and demonstrate reproducible execution.

> This project uses synthetic educational data only. No real patient information is included.

## Objective

This project demonstrates how to:

- write a Dockerfile
- use a Python base image
- copy source code and CSV data into an image
- build a custom Docker image
- run the image as a container
- verify container output and logs
- understand build-time vs runtime behavior
- connect Docker fundamentals with future AI/ML deployment workflows

## Project Structure

```text
dockerized-patient-vitals-summary/
├── Dockerfile
├── patient_summary.py
├── patient_vitals.csv
├── README.md
├── .gitignore
└── SUBMISSION_NOTES.md
```

## Dataset

```csv
patient_id,systolic,diastolic,heart_rate
P001,120,80,72
P002,130,85,78
P003,118,76,68
P004,140,90,82
P005,125,81,75
```

## Expected Output

```text
=============================================
PATIENT VITALS SUMMARY
=============================================
Total patient records : 5
Average systolic BP   : 126.60 mmHg
Average diastolic BP  : 82.40 mmHg
Average heart rate    : 75.00 bpm
=============================================
Data type: Synthetic educational data
```

## Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY patient_summary.py .
COPY patient_vitals.csv .

CMD ["python", "patient_summary.py"]
```

## Dockerfile Explanation

- `FROM python:3.12-slim` — provides the Python runtime.
- `WORKDIR /app` — sets the working directory inside the image.
- `COPY ...` — copies the Python script and CSV file into the image.
- `CMD ["python", "patient_summary.py"]` — runs the script when the container starts.

## Build the Image

```bash
docker build -t patient-vitals-summary .
```

## Verify the Image

```bash
docker images
```

## Run the Container

```bash
docker run --name patient-summary-run patient-vitals-summary
```

## Verify Container Status

```bash
docker ps -a
```

A successful run should show `Exited (0)`.

## View Logs

```bash
docker logs patient-summary-run
```

## Docker Workflow

```text
Dockerfile
   ↓
docker build
   ↓
Docker Image
   ↓
docker run
   ↓
Container
   ↓
Python Script Executes
   ↓
Summary Printed
   ↓
Container Exits
```

## Reproducibility Demonstration

The cloud host did not provide `python3` directly, but the application still executed successfully inside the Docker container because the image used `python:3.12-slim`.

This demonstrates that the required runtime can be packaged inside the image instead of being installed manually on the host.

## RUN vs CMD

`RUN` executes while building an image.

```dockerfile
RUN pip install pandas
```

`CMD` executes when the container starts.

```dockerfile
CMD ["python", "patient_summary.py"]
```

In simple terms:

```text
RUN → build time
CMD → runtime
```

## Image vs Container

```text
Dockerfile → Image → Container
```

An image is a reusable template. A container is an instance created from that image.

## Relevance to AI / ML

The same pattern can later be used for:

```text
ML Model
   ↓
FastAPI
   ↓
Python + ML Libraries
   ↓
Dockerfile
   ↓
Docker Image
   ↓
Container
   ↓
Cloud / Server
```

Useful for ML model serving, reproducible experiments, MLOps, CI/CD, and cloud deployment.

## Challenges

### Docker Registry Timeout
An earlier cloud-lab attempt experienced a Docker Hub timeout. This was an external network/registry issue, not a code or Dockerfile issue.

### Missing Python on Host
The Codespaces host did not have `python3`, but the container ran successfully because the image included Python.

## Commands Used

```bash
docker build -t patient-vitals-summary .
docker images
docker run --name patient-summary-run patient-vitals-summary
docker ps -a
docker logs patient-summary-run
```

## Technologies

- Docker
- Dockerfile
- Python 3.12
- CSV
- Linux
- Git
- GitHub
- GitHub Codespaces

## Data Privacy

This repository contains synthetic educational data only.

## Future Improvements

- add `requirements.txt`
- use Pandas
- accept CSV input at runtime
- use Docker volumes
- add validation
- convert to FastAPI
- containerize an ML model
- publish image to a registry
- use Docker Compose

## Internship Context

Completed as part of the CMIT AI Internship Docker milestone.

```text
Using public Docker images
        ↓
Writing a Dockerfile
        ↓
Building a custom image
        ↓
Running a custom container
```

## Author

**Zameer Hassan Shah**  
Software Engineer | Applied AI/ML

LinkedIn: https://www.linkedin.com/in/zameer-hassan-shah  
Portfolio: https://zameer-portfolio-jade.vercel.app/
