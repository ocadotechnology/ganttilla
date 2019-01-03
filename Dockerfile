################################
##           BUILDER          ##
################################
FROM node:8-alpine as builder

WORKDIR /ganttilla

ADD . .

RUN npm install && npm run-script build

################################
##           RUNNER           ##
################################
FROM nginx:1.15.8-alpine as runner

EXPOSE 80

COPY --from=builder /ganttilla/dist/ganttilla /usr/share/nginx/html

ADD scripts /ganttilla/scripts
ADD docker /ganttilla/docker

RUN apk add --update python3 \
    && pip3 install --upgrade pip \
    && pip3 install -r /ganttilla/scripts/requirements.txt \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/share/nginx/html/assets/descriptors /ganttilla/descriptors \
    && ln -s /ganttilla/docker/gitlab.sh /usr/local/bin/gitlab \
    && ln -s /ganttilla/docker/github.sh /usr/local/bin/github

CMD ["nginx", "-g", "daemon off;"]
