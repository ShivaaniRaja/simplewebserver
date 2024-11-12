from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1 allign="center">SYSTEMPROPERTIES(R.SHIVAANI-24007075)</h1>
        <ol type="I" start="1">
          <li>DeviceName-SHIVAANI23</li>
          <li>Processor-13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
          <li>Installed RAM-8.00 GB (7.69 GB usable)</li>
          <li>Device ID-3A15EDD1-4DE6-4B6C-A2E3-363EDCB59BE0</li>
          <li>Product ID-00342-42644-64747-AAOEM</li>
    </ol>


    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()