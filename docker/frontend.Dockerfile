# docker/fronend.Dockerfile
FROM node:20-slim

WORKDIR /app

# install dependencies (copy package files first)
COPY package*.json /app/

RUN npm ci

# copy app source
COPY . /app/

EXPOSE 5173

# dev server
CMD [ "npm", "start"]