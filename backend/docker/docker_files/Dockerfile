FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN set -e; \
    apt-get update && \
    apt-get -y install netcat-traditional gettext && \
    python -m pip install --upgrade pip && \
    python -m pip install httpie flask


RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r /code/requirements.txt ;\
    chmod +x /code/docker/entrypoints/entrypoint.sh ;

EXPOSE 8000
ENTRYPOINT ["/code/docker/entrypoints/entrypoint.sh"]