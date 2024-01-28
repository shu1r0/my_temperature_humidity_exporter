FROM python:3.10

RUN apt-get update && apt install -y i2c-tools python3-smbus

COPY ../requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app/
