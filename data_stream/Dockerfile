# Use an official Python runtime as a parent image - for a list of others see https://hub.docker.com/_/python/
FROM python:3-stretch

# Set the working directory to /app - this is a directory that gets created in the image
WORKDIR /data_stream

# Copy the current host directory contents into the container at /app
COPY . /data_stream

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Run data_stream_server.py when the container launches
CMD ["python", "data_stream_server.py"]

