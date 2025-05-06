# syntax=docker/dockerfile:1
FROM python:3.12-alpine3.21

ENV WORKDIR=/opt/aviumlabs/app
ENV VIRTUAL_ENV=/opt/aviumlabs/venv
ENV BUILD_ENV=/opt/aviumlabs

RUN set -eux; \
   addgroup -g 935 -S aviumlabs; \
   adduser -u 935 -S -D -G aviumlabs -H -h /opt/aviumlabs -s /bin/ash aviumlabs; \
   install --verbose --directory --owner aviumlabs --group aviumlabs --mode 1755 /opt/aviumlabs
   
RUN apk add --no-cache \
   openssl \
   make \
   gcc \
   musl-dev \
   fuse3 \
   postgresql17-client \
   inotify-tools \
   git

USER aviumlabs

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY .gitignore "${BUILD_ENV}"
COPY pyproject.toml "${BUILD_ENV}"
COPY README.md "${BUILD_ENV}"

CMD [ "python" ]