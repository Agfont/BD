FROM python:3

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN chmod u+x -R .

COPY . /app/

EXPOSE 8090