FROM python:3.8-slim-buster
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
ADD consumer.py /
CMD [ "python" ,"/consumer.py"]
ENV PYTHONUNBUFFERED 1
EXPOSE 8050