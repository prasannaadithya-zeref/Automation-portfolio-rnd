# 🐳 Docker for Automation
*Eliminate "It works on my machine".*

## What is Docker?
It packs your OS, Python, and Chrome into a single file called a "Image".

## 1. The Dockerfile
Create a file named `Dockerfile` (no extension).

```dockerfile
# Start with a base of Python 3.9
FROM python:3.9-slim

# Install Chrome (for Selenium/Robot)
RUN apt-get update && apt-get install -y chromium-driver

# Set the work folder
WORKDIR /app

# Copy our code
COPY . /app

# Install libraries
RUN pip install -r requirements.txt

# Command to run when container starts
CMD ["python", "run_portfolio_demo.py"]
```

## 2. Building & Running
```bash
# Build the image (Pack the box)
docker build -t my-automation-bot .

# Run the container (Ship the box)
docker run my-automation-bot
```

## Why learn this?
In a real job, Jenkins runs your tests inside Docker. If you know Docker, you can debug the CI pipeline locally!
