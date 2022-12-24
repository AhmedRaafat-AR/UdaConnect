FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY . /person-api

WORKDIR /person-api

RUN pwd; ls;

RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["flask", "run", "--host", "0.0.0.0"]