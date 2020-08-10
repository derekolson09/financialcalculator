FROM node:carbon-slim

RUN apt-get -y update \
  && apt-get install -y git

RUN npm install -g @vue/cli

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

USER node

CMD ["npm", "run", "serve"]



#### BUILD VERSION OF DOCKERFILE

# FROM node:lts-alpine

# install simple http server for serving static content
# RUN npm install -g http-server

# # install the vue CLI
# RUN npm install -g @vue/cli

# # make the 'app' folder the current working directory
# WORKDIR /app

# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package*.json ./

# # install project dependencies
# RUN npm install

# # copy project files and folders to the current working directory (i.e. 'app' folder)
# COPY . .

# # build app for production with minification
# RUN npm run build

# # EXPOSE 8080
# CMD [ "http-server", "dist" ]


# run docker-compose build
# run docker-compose up
# in another terminal:
# cd into /rapidquote/frontend
# run docker ps
# get the id for the vue container
# then run docker-exec {conatiner id} npm run serve
