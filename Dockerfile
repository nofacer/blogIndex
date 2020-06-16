FROM python:3.7-alpine

COPY *.py ./
COPY requirements.txt .


RUN apk update
RUN apk add --no-cache git
RUN pip install -r requirements.txt

EXPOSE 8080

CMD python main.py