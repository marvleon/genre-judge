FROM python:3.9

# ODIN marvleon maintainer of the container image
LABEL maintainer="marvleon@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN apt update -y && apt install -y python3-pip && pip3 install -r requirements.txt
# Set PYTHONPATH to include /app directory
ENV PYTHONPATH /app
# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app