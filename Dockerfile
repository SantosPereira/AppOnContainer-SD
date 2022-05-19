FROM python:3.8
WORKDIR /home/app
VOLUME ./ ./
CMD python3 app.py