FROM node:22-bookworm
WORKDIR /opt/patrol
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts --omit=dev && npm rebuild better-sqlite3
COPY src ./src
COPY bin ./bin
COPY client_bridge.mjs client_bridge.test.mjs wnacg.import.js ./
COPY client-profiles ./client-profiles
RUN node --test client_bridge.test.mjs
ENV HOME=/tmp
ENTRYPOINT ["node", "/opt/patrol/bin/venera-patrol.js"]
