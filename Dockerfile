FROM python:3-alpine

ENV PYTHONPATH=/home/det:$PYTHONPATH \
    WORKERS=2
    
WORKDIR /home/det

COPY requirements.txt /home/det
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /home/det

COPY ./credentials.json /home/det/.credentials.json
RUN chmod 600 /home/det/.credentials.json

VOLUME /home/det

EXPOSE 9999

ENTRYPOINT ["python"]
CMD ["/home/det/det/bin/det", "runserver", "-d"]
