FROM python:3.7-alpine
USER ROOT

COPY *.py ./
COPY requirements.txt .


RUN apk update
RUN apk add --no-cache git
RUN pip install -r requirements.txt

USER 1001
CMD python main.py