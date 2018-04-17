FROM node:9-alpine

WORKDIR /app
ADD ./package*.json /app/
RUN npm install
ADD . /app

EXPOSE 8080

CMD npm install && npm run dev
