from flask import Flask, jsonify, request, render_template
import json
from typing import List
from math import radians, sin, cos, acos

import sys

""" Configuration data """
RADIUS_EARTH = 6371
MAX_DISTANCE = 3
QUERY_MIN_LENGTH = 1

app = Flask(__name__)

def check_distance(coordinates: List[float], lat: float, lon: float) -> bool:
	""" Check that the restaurant is within the search radius """
	lat, lon, r_lat, r_lon = map(
		radians,
		[lat, lon, coordinates[1], coordinates[0]]
		)

	distance = RADIUS_EARTH * acos(
		sin(lat) * sin(r_lat) +
		cos(lat) * cos(r_lat) * (cos(lon) - cos(r_lon))
		)

	print(distance, file=sys.stderr)

	if distance < MAX_DISTANCE:
		return True
	else:
		return False


def check_query(restaurant: dict, query: str) -> bool:
	""" Check that the search query is found within the restaurant data """
	query = query.lower()

	if query in restaurant["name"].lower() or\
		query in restaurant["description"].lower():
		return True
	
	else:
		for tag in restaurant["tags"]:
			if query in tag.lower():
				return True
		return False


def get_valid_restaurants(restaurants: List[dict],
							query: str,
							lat: float,
							lon: float) -> List[dict]:
	""" Get list of restaurants that match the search distance and query """
	valid_restaurants = []

	for restaurant in restaurants:
		if check_distance(restaurant["location"], lat, lon) and\
			check_query(restaurant, query):
			valid_restaurants.append(restaurant)

	return valid_restaurants

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/restaurants/search", methods=["GET"])
def restaurant_search():
	try: # Validating input data
		query = str(request.args.get("q"))
		lat = float(request.args.get("lat"))
		lon = float(request.args.get("lon"))
	except ValueError:
		return jsonify("Invalid input")
	
	if len(query) < QUERY_MIN_LENGTH:
		return jsonify(
			f"Search query too short (minimum {QUERY_MIN_LENGTH} character{int(bool(QUERY_MIN_LENGTH - 1))}"
			)

	# No DB allowed
	try:
		with open ("restaurants.json") as f:
			restaurants_list = json.load(f)["restaurants"]
	except:
		return jsonify("Couldn't get restaurants")

	restaurants = get_valid_restaurants(restaurants_list, query, lat, lon)

	return jsonify(restaurants)


if __name__ == "__main__":
	app.run()