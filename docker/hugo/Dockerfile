FROM golang:1.11

ENV HUGO_VERSION v0.53
ENV SITE_HOME /site

RUN git clone --depth 1 --branch ${HUGO_VERSION} https://github.com/gohugoio/hugo.git \
 && cd hugo \
 && go install \
 && cd ../ \
 && rm -rf hugo pkg

WORKDIR ${SITE_HOME}

ENTRYPOINT ["hugo"]
