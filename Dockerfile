# syntax=docker/dockerfile:1
FROM python:3.13-alpine3.22

ENV WORKDIR=/opt/python/app
ENV VIRTUAL_ENV=/opt/python/venv
ENV BUILD_ENV=/opt/python

RUN set -eux; \
   addgroup -g 935 -S python; \
   adduser -u 935 -S -D -G python -H -h /opt/python -s /bin/ash python; \
   install --verbose --directory --owner python --group python --mode 1755 /opt/python
   
RUN apk add --no-cache \
   openssl \
   make \
   gcc \
   musl-dev \
   fuse3 \
   postgresql17-client \
   inotify-tools \
   git

USER python

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY .gitignore "${BUILD_ENV}"
COPY pyproject.toml "${BUILD_ENV}"
COPY README.md "${BUILD_ENV}"

CMD [ "python" ]