#!/usr/bin/env python
# coding: utf-8

# In[3]:


import http.server
import socketserver

PORT = 2305
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# In[7]:


import http.server
import socketserver
import ssl

PORT = 2305
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile = "C:\\Users\\hp\\Desktop\\privatekey.key",
                                   certfile = "C:\\Users\\hp\\Desktop\\certificate.crt",
                                   server_side=True)
    httpd.serve_forever()


# In[ ]:
