# Use an existing image as the base
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the necessary packages
RUN pip install -r requirements.txt

# Copy the webserver file
COPY webserver.py .

# Copy the index.html file
COPY index.html .

# Expose port 80
EXPOSE 80

# Run the webserver on port 80
CMD ["python", "webserver.py"]
