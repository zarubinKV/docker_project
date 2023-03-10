FROM python:latest

RUN mkdir /writer
RUN pip install --no-cache-dir mysql-connector-python

ADD main.py /writer/
ADD index.html /writer/

WORKDIR /writer

EXPOSE 8080

CMD ["python", "main.py"]
