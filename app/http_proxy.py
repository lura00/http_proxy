import socketserver
from http import server
import urllib.request
from urllib.parse import urlparse, urlunparse
from flask import redirect, request
import webbrowser

PORT = 8000
# http://localhost:8000/http://httpvshttps.com
# http://httpvshttps.com
BLOCK_DOMAIN = 'http://httpvshttps.com'

class MyProxy(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # print('request received from browser')
        url = self.path[1:]
        if url == BLOCK_DOMAIN:
            newurl = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            webbrowser.open(newurl)
            self.wfile.write('Bad website'.encode())
            self.send_response(307)
        # Headers send cookies, session data etc
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)

httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print("listening...")
httpd.serve_forever()

FROM_DOMAIN = MyProxy()
TO_DOMAIN = 'https://youtube.com'

def redirect_to_new_domain():
    urlparts = urlparse(request.url)
    if urlparts.netloc == FROM_DOMAIN:
        urlparts_list = list(urlparts)
        urlparts_list[1] = TO_DOMAIN
        return redirect(urlunparse(urlparts_list), code=301)
