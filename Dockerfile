FROM python:3-alpine

ENV PYTHONPATH=/home/det:$PYTHONPATH \
    WORKERS=2
    
WORKDIR /home/det

COPY requirements.txt /home/det
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /home/det

VOLUME /home/det

EXPOSE 8888

ENTRYPOINT ["python"]
CMD ["/home/det/det/bin/det", "runserver", "-d"]

