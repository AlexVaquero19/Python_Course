# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
