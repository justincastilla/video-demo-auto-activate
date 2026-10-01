// The dev server the video's `api` service runs. `curl localhost:3000` prints:
// {"status":"ok","service":"api"}
const http = require("http");

http
  .createServer((req, res) => {
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify({ status: "ok", service: "api" }) + "\n");
  })
  .listen(3000);
