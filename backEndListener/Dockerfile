# Use an official Python image as the base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the script to the working directory
COPY server.py .

# Install the required packages
RUN pip install Flask
RUN pip install requests

# Specify the command to run the script
CMD ["python", "server.py"]