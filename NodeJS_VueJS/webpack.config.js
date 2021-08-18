const nodeExternals = require('webpack-node-externals');

module.exports = {
	entry: './index.js',
	output: { filename: './server.js'},
    target: 'node',
    externals: [nodeExternals()]
}