FROM node:10.15.3-alpine

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY . .

CMD npm run watch