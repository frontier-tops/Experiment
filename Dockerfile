# Use official Python slim-buster image
FROM python:3.11-slim-buster

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libssl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Streamlit application
COPY app.py ./

# Expose Streamlit default port
EXPOSE 8501

# Set environment variables to mask sensitive information
ENV ENDPOINT_URL=""
ENV API_TOKEN=""

# Command to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
