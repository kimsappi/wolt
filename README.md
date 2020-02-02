# About
Pre-assignment for Wolt summer 2020 internships. It was only required to complete either the front-end or back-end assignment, but I did both to facilitate learning.

# Back-end
The back-end assignment was to make an API that returns a list of restaurant objects matching a query string and located less than 3 km from the query coordinates. Restaurant data was given as a JSON file and we were instructed not to use any kind of database.

I decided to implement the API with Python Flask. Flask includes a built-in web server (not suitable for production...), so installation is really simple. There's also a very simple web interface, which allows easy querying of the API.

## Running the server
There are 2 ways to run the API: Python and Docker. These instructions are for *NIX systems, other operating systems are available.

### Option 1: Python
Requires Python 3 to be installed (e.g. `sudo apt-get install python3`).
```shell
git clone https://github.com/kimsappi/wolt.git wolt
cd wolt/backend
pip3 install flask
python3 app.py
```

### Option 2: Docker
Requires Docker to be installed (e.g. `sudo apt-get install docker`).
```shell
git clone https://github.com/kimsappi/wolt.git wolt
cd wolt/backend
docker build -t wolt:flask .
docker run --rm -p 5000:5000 wolt:flask
```

