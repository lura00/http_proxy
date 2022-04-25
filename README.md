# HTTP proxy written in Python

## To start:
- Install dependencies, pip install -r requirements.txt.
- go to browser settings, often under "general" or "network", go to Network Settings.
- (in firefox) a "connection settings" will pop up, in the area "Configure Proxy Access tot he Internet",
    Set to "Manual proxy conf" and in the box called "HTTP Proxy" do the changes below.
- Enter localhost and listening port same as in the python program.
- python3 app/proxy_server.py to execute the program.
- Listening port in browser must be the same as in the python script.

## Go to a http-test-site 
- I have been testing my proxy on http://httpvshttps.com
- To browse a http-website through the proxy server you need to go to localhost and port that has been set.
- To do this, enter this in browser search box: localhost:8000/http://httpvshttps.com.
- HTTPS websites will still work.


## Block a website
- Add a website to the database, or check if the website is already in the database.
- If a website is in the database that site should be blocked and close the connection.
- See the db.py file all the functions for sprint 2 should already be implemented. 
    A nice cli gui is needed to ask the user what he/she/non-binary wants to do with blocks etc.
- Right now you can only check the content of the database manually, not with a nice interface.
- To do so, start sqlite3 and enter db name. "sqlite3 blocks.db" .c blocks.db (to make sure tou are connected).
- to see the content of the table in the database, SELECT * FROM blocks; (in my case the table is also called blocks).


## Database
- The database file is pretty much ready to go. As we can see in the http_proxy-file I have imported from the db-file the class    that contains all the options for the db.
- I have assigned the class to a variable in the http_proxy-file called database.
- To use the db-functions. just type databse. and choose the needed funtion.
- To get the databse and table created use the commented code in the http_proxy-file, "database.create_table()" and a db and table will be created.


## Dockerfile
- To buid image "docker build -t name:tag .
- To start container "docker run -p 8000:8000 -it --rm name:tag
- If you beeing refused connection by Docker daemon, try type in cli, sudo chmod 666 /var/run/docker.sock

## Github/workflows (pipeline)
- Lints the code base on the first part
- The other part is "push to production" or at least image to Dockerhub for public use.
- The github actions file "build-deploy.yml" uses Dockerfile to build the image then push it. 
- The code is from docs.docker, see link if interesting.
- https://docs.docker.com/ci-cd/github-actions/

## Testing
- Uses pytest
- No tests has been made, still trying to figure out how to start.
- I have an idea to check the response code that we get the correct ones.
- possible import requests, and the other files from /app.


# TO-DO (sprint2)


## Create a client CLI-based is enough.
### funcitons for client
- add a website to block
- change website-blocks
- delete website-blocks

## Stats
- Fetch data from database how many times a certain website has been blocked.

## Tests
- Write tests that are missing

## README
- Add the functions you have written to the README for future use.


# Extras
- Add HTTPS-proxy
- Hide your personal IP with proxy.
