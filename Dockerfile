FROM python:3.8
WORKDIR /home/app
COPY ./ ./
RUN pip install -r requirements.txt
CMD ptyhon3 src/util/CursorBD.py && python3 app.py