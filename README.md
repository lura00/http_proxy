## HTTP proxy written in Python

# To start:
- go to browser settings change header called something like "manual proxy".
- Enter localhost and listening port same as in the python program.
- python3 app/proxy_server.py.
- Listening port in browser must be the same as in the python script.
    In firefox go to settings, general, scroll to bottom to network settings. Set "manual proxy configuration" enter in "http proxy" localhost or 127.0.0.1 and port same as in the python script.

# Go to a http-test-site 
- I have been testing my proxy on http://httpvshttps.com
- To browse a http-website through the proxy server you need to go to localhost and port that has been set.
- To do this, enter this in browser search box: localhost:8000/http://httpvshttps.com


# Block a website
- Add a website to the database, or check if the website is already in the database.
- If a website is in the database that site should be blocked and close the connection.
- See the db.py file all the functions for sprint 2 should already be implemented. 
    A nice cli gui is needed to ask the user what he/she/non-binary wants to do with blocks etc.


# Dockerfile
- To buid image "docker build -t name:tag .
- To start container "docker run -it --rm name:tag
