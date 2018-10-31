const path = require("path")

module.exports = {
  resolve: {
    alias: {
      common: path.resolve(__dirname, "ffba/react-js/common/"),
      prod: path.resolve(__dirname, "prod/react-js/prod/"),
      sales: path.resolve(__dirname, "sales/react-js/sales"),
    }
  },
  entry: {
    sales: "./sales/react-js/sales.js",
  },
  output: {
    path: __dirname + "/ffba/static/bundles",
    filename: "ffba-[name].bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules)/,
        use: {
          loader: "babel-loader",
        }
      }
    ]
  }
}
