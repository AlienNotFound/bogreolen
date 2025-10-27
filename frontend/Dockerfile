# FROM node:22-alpine AS builder
# WORKDIR /code
# COPY ./frontend/package*.json ./
# RUN npm ci
# COPY ./frontend .
# RUN npm run build
# RUN npm prune --production

# FROM node:22-alpine
# WORKDIR /code
# COPY --from=builder /code/build build/
# COPY --from=builder /code/node_modules ./node_modules
# COPY ./frontend/package.json ./
# EXPOSE 3000
# ENV NODE_ENV=production
# CMD [ "node", "build" ]

FROM node:22-alpine
WORKDIR /code

COPY ./frontend/package*.json ./
RUN npm install

# COPY ./frontend .

EXPOSE 5173

# CMD ["npm", "run", "dev", "--", "--host", "--watch"]