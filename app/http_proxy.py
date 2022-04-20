import socket,sys,_thread,traceback, ssl

# import SimpleWebSocketServer
# import http.server
# import urllib

 
def main():
    global buffer_size
    try:
        listen_port = int(input("Enter a listening port: "))
    except KeyboardInterrupt:
        sys.exit (0)
        
    max_conn = 1000  # Change buffer size to lower number
    buffer_size = 10000
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", listen_port))
        s.listen(max_conn)
        s.accept()  # Added accept().
        print("[*] Intializing socket. Done.")
        print("[*] Socket binded successfully...")
        print(f"[*] Server started successfully: {format(listen_port)}\n[*] end with ctrl c")
    except Exception as e:
        print(e)
        sys.exit(2)

    while True:
        try:
            conn,addr = s.accept()
            _thread.start_new_thread(conn_string,(conn, addr))  # move conn.recv() and remove data from _thread so it only focuses on new connections
        except KeyboardInterrupt:
            s.close()
            print("\n[*] Shutting down...")
            sys.exit(1)
    s.close()

def conn_string(conn, addr):
    BLACKLIST_DOMAINS = input("Would you like to block any websites? ")
    try: 
        data = conn.recv(buffer_size)
        print(addr)
        first_line = data.decode('latin-1').split("\n")[0]
        print(first_line)
        url = first_line.split(" ")[1]
        
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]
            
        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos + 1):][:webserver_pos - port_pos -1])
            webserver = temp[:port_pos]
        # Check if the host:port is blacklisted and unable connection
        # for i in range(0, len(config['BLACKLIST_DOMAINS'])):
        
        if webserver == BLACKLIST_DOMAINS:
            print("BLACKLIST DOMAIN")
            conn.close()

        print(webserver)
        proxy_server(webserver,port,conn,data,addr)
    except Exception as e:
        print(e)
        traceback.print_exc()
        
def proxy_server(webserver, port, conn, data, addr):
    print("{} {} {} {}".format(webserver, port, conn, addr))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)
        while 1:
            reply = s.recv(buffer_size)
            
            if len(reply) > 0:
                conn.sendall(reply)
                print(f"[*] Request sent: {format(addr[0])} > {format(webserver)}")  # .format(addr[0],webserver)
            else:
                break        
        
        s.close()
        conn.close()
        
    except Exception as e:
        print(e)
        traceback.print_exc()
        s.close()
        conn.close()
        sys.exit(1)

if __name__ == "__main__":
    main()


# PORT = 9012
# class JustAProxy(SimpleHTTPSServer.SimpleWebSocketServer):
#    def do_GET(self):
#       url=self.path[1:]
#       self.send_response(200)
#       self.end_headers()
#       self.copyfile(urllib.urlopen(url), self.wfile)
# httpd = SimpleWebSocketServer.SimpleWebSocketServer('localhost',PORT,JustAProxy)
# print ("Proxy Srever at" , str(PORT))
# httpd.serveforever()

# if it's just a http/https proxy that is configured in the browser, 
# the browser will use the "connect" method when trying to connect to https web sites
# you will not be able to see or filter the content (as it's encrypted), 
# but you will get the hostname and port that the browser is trying to connect to and you can filter on that,
# then then allow or deny the request based on that 
# instead of just handling normal http "get", "push" and friends, 
# your proxy also need to handle the "connect" method for the https requests
