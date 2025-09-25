# docker/fronend.Dockerfile
FROM node:20-alpine

WORKDIR /app

# install dependencies (copy package files first)
COPY package*.json /app/

RUN npm ci

# copy app source
COPY . /app/

EXPOSE 3000

# dev server
CMD [ "npm", "start"]