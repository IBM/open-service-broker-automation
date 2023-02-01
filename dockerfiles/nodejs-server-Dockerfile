FROM node:14

# Create app directory
WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install oas3-tools

# Bundle app source
COPY . .

EXPOSE 3000
CMD [ "node", "index.js" ]
