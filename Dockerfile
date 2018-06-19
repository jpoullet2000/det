FROM python:3-alpine

ENV PYTHONPATH=/home/det:$PYTHONPATH \
    WORKERS=2

WORKDIR /home/det
COPY requirements.txt /home/det
COPY .credentials.json /home/det
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /home/det
ADD .credentials.json /root/.credentials.json

RUN cd /home/det \
    python setup.py install \
    cd -
EXPOSE 9999
ENTRYPOINT ["python"]
CMD ["/home/det/det/bin/det", "runserver", "-d"]
