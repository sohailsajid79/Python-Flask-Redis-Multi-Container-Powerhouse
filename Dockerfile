FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV FLASK-APP=app.py

CMD [ "flask,", "run", "--host=0.0.0.0", "--port=5000" ]