# Use the official Python base image from Docker Hub
FROM python:3.9

# Set a working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "app.py"]
