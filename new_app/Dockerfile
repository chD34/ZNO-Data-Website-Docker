FROM python:3.10.7-slim-buster

WORKDIR /usr/src/new_app

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/new_app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/new_app/

CMD ["python", "new_app.py"]
