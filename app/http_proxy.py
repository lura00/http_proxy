import socketserver
from http import server
import urllib.request
import webbrowser
from db import webBlock_db


"""HTTP PROXY, WEB BLOCKER

    Website I test on:
    localhost:8000/http://httpvshttps.com

    Server running on localhost port 8000. So to test entering a http website enter in the browser
    localhost:8000/http://example.com (example.com is also a test http website)"""

# decalaring the database object from db.py file
database = webBlock_db()

# database.create_table()

# add a website to tabel in database

# database.add_one('http://httpvshttps.com', 'www.httpvshttps.com')

PORT = 8002
BLOCK_DOMAIN = database.show_all_blockes()
print(f"This is all the blocked domains: {BLOCK_DOMAIN}")


class MyProxy(server.SimpleHTTPRequestHandler):

    # def __init__(self, *args, database, **kwargs):
    #     super().__init__(*args, database, **kwargs)
    #     self._database = database

    def redirect_to_new_website(self):
        """Simple function to redirect user to another 
        website when trying to enter a blocked domain.
        """
        newUrl = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        print("redirecting due to banned website")
        return newUrl

    def do_GET(self):
        """Connection function
            Fetching the URL from path.
            checks if the URL is in BLOCK_DOMAIN.
            If all is good, sends response and header and connects."""
        # print('request received from browser')
        # BLOCK_DOMAIN = self._database.show_all_blockes()
        # print(f"This is all the blocked domains: {BLOCK_DOMAIN}")
        url = self.path[1:]
        if url in BLOCK_DOMAIN:
            newurl = self.redirect_to_new_website()
            webbrowser.open(newurl)
            # url = newurl
            self.wfile.write('Bad website'.encode())
            self.send_response(307)

        # Headers send cookies, session data etc
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)


"""httpd
    Fetching the URL from conn-class and do_GET function,
    Then printing listening to let the user know the server is active,
    Then uses the serve_forever module. And only breaks the connection when user stops it, with command, ctrl + C"""

httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print("listening...")
httpd.serve_forever()

# def main():
#     # res = functools.partial(MyProxy, database=webBlock_db())
#     httpd = socketserver.ForkingTCPServer(('', PORT), functools.partial(MyProxy, database=webBlock_db()))
#     print("listening...")
#     httpd.serve_forever()
#     return 0

# if __name__ == "__main__":
#     sys.exit(main())

# FROM_DOMAIN = MyProxy()
# TO_DOMAIN = 'https://youtube.com'
# from urllib.parse import urlparse, urlunparse
# from flask import redirect, request
# def redirect_to_new_domain():
#     urlparts = urlparse(request.url)
#     if urlparts.netloc == FROM_DOMAIN:
#         urlparts_list = list(urlparts)
#         urlparts_list[1] = TO_DOMAIN
#         return redirect(urlunparse(urlparts_list), code=301)
