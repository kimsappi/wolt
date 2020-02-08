# About
Pre-assignment for Wolt summer 2020 internships. It was only required to complete either the front-end or back-end assignment, but I did both to facilitate learning. The main front-end interface is not connected to the back-end in any way, since the scope was slightly different.

# Back-end
The back-end assignment was to make an API that returns a list of restaurant objects matching a query string and located less than 3 km from the query coordinates. Restaurant data was given as a JSON file and we were instructed not to use any kind of database.

I decided to implement the API with Python Flask. Flask includes a built-in web server (not suitable for production...), so installation is really simple. There's also a very simple web interface, which allows easy querying of the API.

## Running the server
There are 2 ways to run the API: Python and Docker. These instructions are for *NIX systems, other operating systems are available.

### Option 0: Pre-deployed (limited time)
The API is available for a limited time at https://gcr-vr4fnhk7fa-uc.a.run.app/

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

## Querying the API
The API requires 3 parameters:
* *q* (string): Search string to be searched for in the restaurant's name, description and tags (case insensitive). *Minimum length 1 character per the assignment, empty string considered invalid.*
* *lat* (float): Latitude of the location to be searched around in degrees.
* *lon* (float): Longtitude of the location to be searched around in degrees.

Queries are possible with both `GET` and `POST` requests.

### Option 1: Web interface
Go to either http://localhost:5000 (Docker, possibly Flask) or http://0.0.0.0:5000 (Flask) and you should be presented with an interface like this:

![User interface](/images/interface.png)

This allows you to enter the search string and coordinates for the query. The query response is rendered below as well as in the browser console.

### Option 2: Browser URL insertion, curl, etc.
The API responds to queries at `$URL/restaurants/search`. You can perform `GET` requests by entering the URL in the following command into your browser or using curl:
```shell
curl 'http://localhost:5000/restaurants/search?q=classic&lat=60.17&lon=24.94'
```
And `POST` requests with the following command:
```shell
curl -d 'q=classic&lat=60.17&lon=24.94' http://localhost:5000/restaurants/search
```
While the API is case insensitive, it is MIME type sensitive, so stick to -d (`application/x-www-form-urlencoded`).

# Front-end
The goal was to display 50 restaurants defined as JSON objects, with ascending and descending sort functionality.

My implementation is a React-based web front-end. React was a recommendation by Wolt, although the assignment would have been possible to complete without it. I didn't feel the project necessitated using a CSS framework, so I completed it without one.

## Dependencies
* React & ReactDOM
* Babel (JSX)
* jQuery

## Using the implementation
All dependencies are included and there's no transpilation necessary. Thus running the project is easy. There are a few options:

### Option 0: Pre-deployed (limited time)
The front-end solution is available for a limited time at https://gcr-vr4fnhk7fa-uc.a.run.app/frontend

### Option 1: Easy
1. `git clone https://github.com/kimsappi/wolt.git wolt`
2. Open `wolt/frontend/index_safe.html` in your favourite browser. `index_safe.html` is a messy file, but one that can be run successfully without a web server.

### Option 2: Harder
1. `git clone https://github.com/kimsappi/wolt.git wolt`
2. `cd wolt/frontend`
3. Open a web server (e.g. `python -m SimpleHTTPServer`) and navigate to the front page (e.g. http://localhost:8000)
