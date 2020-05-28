const FileManagerPlugin = require("filemanager-webpack-plugin-fixed");

module.exports = {
  transpileDependencies: ["vuetify"],

  devServer: {
    proxy: "http://192.168.0.64:8000", // xhr only
    index: "home.html",
  },

  outputDir: "dist",
  publicPath: "/",
  assetsDir: "static",

  pages: {
    home: {
      entry: "src/pages/main_home.js",
      filename: "home.html",
      template: "public/index.html",
      title: "WpackMultiThree/home.html",
      minify: false,
    },
    post_list: {
      entry: "src/pages/main_post_list.js",
      filename: "post_list.html",
      template: "public/index.html",
      title: "WpackMultiThree/post_list.html",
      minify: false,
    },
    post_detail: {
      entry: "src/pages/main_post_detail.js",
      filename: "post_detail.html",
      template: "public/index.html",
      title: "WpackMultiThree/post_detail.html",
      minify: false,
    },
  },

  configureWebpack: {
    plugins: [
      new FileManagerPlugin({
        onStart: {
          delete: ["../back/static/**/", "../back/templates/**/"],
        },

        onEnd: {
          copy: [
            {
              source: "dist/static",
              destination: "../back/static/",
            },
            {
              source: "dist/favicon.ico",
              destination: "../back/static/img/",
            },
            {
              source: "dist/home.html",
              destination: "../back/templates/",
            },
            {
              source: "dist/post*.html",
              destination: "../back/templates/blog/",
            },
          ],
        },
      }),
    ],
  },
};
