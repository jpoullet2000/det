FROM python:3-alpine

ENV PYTHONPATH=/home/det:$PYTHONPATH

WORKDIR /home/det

COPY requirements.txt /home/det
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /home/det
COPY det /usr/local/bin

VOLUME /home/det

EXPOSE 8888

ENTRYPOINT ["python"]
CMD ["-c", "from det import cli; cli.runserver()"]
