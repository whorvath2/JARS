FROM python:3.13

ARG guid
ARG uuid

RUN apt-get update
RUN apt-get install -y nginx supervisor r-base

RUN groupadd -g $guid api-service \
    && useradd --no-log-init -d /service/jars -s /bin/bash -u $uuid -g $guid api-service \
    && mkdir -p /service/jars \
    && chown -R api-service:api-service /service/jars

WORKDIR /service/jars
COPY . /service/jars
COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisord.conf

ENV VIRTUAL_ENV=.venv
RUN python -m venv "$VIRTUAL_ENV" \
    && "$VIRTUAL_ENV"/bin/python -m pip install --upgrade pip \
    && "$VIRTUAL_ENV"/bin/pip install uv \
    && "$VIRTUAL_ENV"/bin/uv build \
    && "$VIRTUAL_ENV"/bin/pip install .[container] \
    && "$VIRTUAL_ENV"/bin/pip install dist/*.whl

ENV PATH=$PATH:$VIRTUAL_ENV/bin

EXPOSE 80
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/service/jars/supervisord.conf"]
