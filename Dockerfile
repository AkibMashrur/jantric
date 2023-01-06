# Start from python base image
FROM python:3.8

# Set working directory to /code
WORKDIR /code

# Copy requirements.txt to /code
COPY ./requirements.txt /code/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app to /code
COPY ./app /code/app

# Run uvicorn with proxy headers and bind to port 80
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
