
ln -s /etc/jest/node_modules ${CYBER_DOJO_SANDBOX}/node_modules

npm run lint
npm run test
