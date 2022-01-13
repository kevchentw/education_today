FROM python

EXPOSE 5000

RUN apt-get update && apt-get install -y default-mysql-client && apt-get clean

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["flask", "run", "--host", "0.0.0.0"]