const path = require("path");
const webpack = require("webpack");

let config = {
    entry: "./src/index.tsx",
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
    }
};

module.exports = (env, args) => {
    if (args.mode === "development") {
      config.devtool = "source-map";
      config.devServer = {
        contentBase: path.join(__dirname, "public/"),
        port: 3000,
        publicPath: "http://localhost:3000/dist/",
        hotOnly: true
      },
      config.plugins = [new webpack.HotModuleReplacementPlugin()]
    }

    config.mode = args.mode

    return config;
};