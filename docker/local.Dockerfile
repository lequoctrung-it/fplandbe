# pull official base image
FROM python:3.11.4-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint script and wait-for-it script
COPY ../entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# copy project
COPY ../ .

#RUN python manage.py migrate
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]