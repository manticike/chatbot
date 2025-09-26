# docker/backend.Dockerfile

FROM python:3.10-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# copy application code (from build context)
COPY ./backend /app


# Expose port
EXPOSE 8000

# Run app with Gunicorn
CMD [ "gunicorn", "chatbot.wsgi:application", "--build", "0.0.0.0:8000"]