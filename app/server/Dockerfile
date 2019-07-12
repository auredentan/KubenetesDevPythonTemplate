FROM node:10.15.3-alpine as front-build

COPY frontend/package.json package.json
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.7.3-alpine3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY server/requirements.txt server/requirements.txt
RUN pip install -r server/requirements.txt

COPY server server
COPY --from=front-build index.html frontend/index.html
COPY --from=front-build ./dist frontend/dist

CMD gunicorn --workers=1 --bind=0.0.0.0:8080 server.src.app:app
