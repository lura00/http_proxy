## HTTP proxy written in Python

# To start:
- go to browser settings change header called something like "manual proxy".
- Enter localhost and listening port same as when you start the python program.
- python3 app/proxy_server.py.
- Enter listening port, same as in browser settings.
    In firefox go to settings, general, scroll to bottom to network settings. Set "manual proxy configuration" enter in "http proxy" localhost or 127.0.0.1 and port same as enter when you start the program.

# Go to a http-test-site 
- I have been testing my proxy on http://httpvshttps.com


# Block a website
- Add a website to the database, or check if the website is already in the database.
- If a website is in the database that site should be blocked and close the connection.
