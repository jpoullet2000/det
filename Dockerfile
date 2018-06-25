FROM python:3-alpine
ARG DET_WEBSERVER_PORT=9999

ENV PYTHONPATH=/home/det:$PYTHONPATH \
    WORKERS=2 \
    DET_WEBSERVER_PORT=${DET_WEBSERVER_PORT}

WORKDIR /home/det
COPY requirements.txt /home/det
COPY .credentials.json /home/det
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /home/det
ADD .credentials.json /root/.credentials.json

RUN cd /home/det \
    python setup.py install \
    cd -
EXPOSE $DET_WEBSERVER_PORT
CMD python /home/det/det/bin/det runserver -p $DET_WEBSERVER_PORT -d
