# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (If you don't have one, we install basics manually)
RUN pip install --no-cache-dir pandas requests robotframework selenium plotly

# Define environment variable
ENV ENVIRONMENT=PRODUCTION
ENV DB_HOST=localhost

# Run the demo script when the container launches
CMD ["python", "run_portfolio_demo.py"]
