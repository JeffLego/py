import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.' #where you html files and cgi-bin script directory live
port = 80 #default http://localhost/, else use http://localhost:xxx

os.chdir(webdir)	#run html in root directory
srvraddr = ("", port)	#my hostname, port number
srvobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvobj.serve_forever()	#run as perpetual daemon