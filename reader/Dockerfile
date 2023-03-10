FROM python:latest

RUN mkdir /reader
RUN pip install --no-cache-dir mysql-connector-python

ADD main.py /reader/

WORKDIR /reader

EXPOSE 8081

CMD ["python", "main.py"]
