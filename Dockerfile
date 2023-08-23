# pull official base image
FROM python:3.8.16


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install setuptools

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["gunicorn", "habit_tracker.wsgi:application"]