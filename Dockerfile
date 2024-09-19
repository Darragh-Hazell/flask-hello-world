FROM python:3.12-alpine

WORKDIR /app

ADD app.py /app
ADD requirements.txt /app
ADD templates /app/templates

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME=World

CMD ["python", "app.py"]