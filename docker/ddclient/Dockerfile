FROM debian:stretch-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      ddclient \
      gettext-base \
 && rm -rf /var/lib/apt/lists/*

CMD ["ddclient"]
