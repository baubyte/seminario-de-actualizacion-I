FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV DIRECTORY=/opt/project

RUN mkdir ${DIRECTORY}
WORKDIR ${DIRECTORY}

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y iputils-ping vim curl gcc python3-dev libpq-dev locales && \
    echo "es_AR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    locale -a && \
    export LC_ALL="es_AR.utf8" && \
    export LC_CTYPE="es_AR.utf8" && \
    locale -a

COPY . ${DIRECTORY}

RUN cd ${DIRECTORY} && python -m pip install -r requirements --no-cache-dir

CMD tail -f /dev/null
