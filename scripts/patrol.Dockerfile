FROM node:22-bookworm
WORKDIR /opt/patrol
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts --omit=dev && npm rebuild better-sqlite3
COPY src ./src
COPY bin ./bin
ENV HOME=/tmp
ENTRYPOINT ["node", "/opt/patrol/bin/venera-patrol.js"]
