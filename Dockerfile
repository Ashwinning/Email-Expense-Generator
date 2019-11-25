FROM madnight/docker-alpine-wkhtmltopdf
RUN \
    apk update \
    apk upgrade \
    apk add bash

RUN /bin/sh -c "apk add --no-cache bash"
