FROM python:3.9-alpine

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project

RUN apk install python3-dev build-essential libmysqlclient-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . /project

RUN mkdir -p logs && mkdir -p /var/log/gunicorn

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]