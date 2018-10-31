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
    sales: "./sales/react-js/sales/SalesApp.js",
  },
  output: {
    path: __dirname + "/ffba/static/bundles",
    filename: "ffba-[name].bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx|mjs)$/,
        exclude: /(node_modules)/,
        use: {
          loader: "babel-loader",
          options: {
            // This is a feature of `babel-loader` for webpack (not Babel itself).
            // It enables caching results in ./node_modules/.cache/babel-loader/
            // directory for faster rebuilds.
            cacheDirectory: true,
          },
        },
      },
      {
        test: /\.css$/,
        use: [
          require.resolve('style-loader'),
          {
            loader: require.resolve('css-loader'),
            options: {
              importLoaders: 1,
            },
          },
          {
            loader: require.resolve('postcss-loader'),
            options: {
              // Necessary for external CSS imports to work
              // https://github.com/facebookincubator/create-react-app/issues/2677
              ident: 'postcss',
              plugins: () => [
                require('postcss-flexbugs-fixes'),
                autoprefixer({
                  browsers: [
                    '>1%',
                    'last 4 versions',
                    'Firefox ESR',
                    'not ie < 9', // React doesn't support IE8 anyway
                  ],
                  flexbox: 'no-2009',
                }),
              ],
            },
          },
        ],
      },
    ]
  }
}
