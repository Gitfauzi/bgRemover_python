# Use Python 3.10 base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY . /app

# Install system dependencies (optional but helpful)
RUN apt-get update && apt-get install -y \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (Streamlit default is 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "bgRemover.py"]
