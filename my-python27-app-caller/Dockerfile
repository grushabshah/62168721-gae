# Use an official Python 2.7 image as the base
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080, which is required for GAE Flex
EXPOSE 8080

# Define the command to run your app
# The entrypoint is already specified in app.yaml, so this is for local testing or as a fallback
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
