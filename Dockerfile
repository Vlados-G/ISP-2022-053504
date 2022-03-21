FROM python:3.8-alpine

#WORKDIR /usr

COPY . .

ENTRYPOINT ["/bin/sh"]