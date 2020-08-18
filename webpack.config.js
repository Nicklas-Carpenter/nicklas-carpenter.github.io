const path = require("path");
const webpack = require("webpack");

module.exports = {
    entry: "./src/index.tsx",
    // mode: "development",
    devtool: "inline-source-map",
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          exclude: /node_modules/,
          use: "ts-loader",
        },
      ]
    },
    resolve: { 
        extensions: [".js", ".jsx", ".ts", ".tsx"] 
    },
    output: {
      // publicPath: "/dist/",
      filename: "bundle.js",
      path: path.resolve(__dirname, "dist")
    },
    devServer: {
      contentBase: path.join(__dirname, "public/"),
      port: 3000,
      publicPath: "http://localhost:3000/dist/",
      hotOnly: true
    },
    plugins: [new webpack.HotModuleReplacementPlugin()]
  };