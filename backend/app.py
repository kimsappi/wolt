import json
import logging
import requests
from math import acos, cos, radians, sin
from typing import List

from flask import Flask, jsonify, render_template, request
#import blurhash

""" Configuration data """
RADIUS_EARTH = 6371
MAX_DISTANCE = 3
QUERY_MIN_LENGTH = 1

app = Flask(__name__)

logging.basicConfig(#filename="wolt.log",
					level=logging.DEBUG,
					format="%(levelname)s: %(asctime)s %(message)s")

def check_distance(coordinates: List[float], lat: float, lon: float) -> bool:
	""" Check that the restaurant is within the search radius """
	# Converting degrees to radians
	lat, lon, r_lat, r_lon = map(
		radians,
		[lat, lon, coordinates[1], coordinates[0]]
		)

	# Great circle distance
	distance = RADIUS_EARTH * acos(
		sin(lat) * sin(r_lat) +
		cos(lat) * cos(r_lat) * cos(lon - r_lon)
		)

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


#def validate_blurhash(restaurant: dict) -> None:
#	""" Logs warning if stored blurhash doesn't match calculated one """
#	try:
#		image = requests.get(restaurant["image"], stream=True)
#	except:
#		logging.warning(f"Couldn't get image for {restaurant['name']}, {restaurant['city']}")
#		return None
#	hash = blurhash.encode(image.raw, x_components=4, y_components=3)
#	if restaurant["blurhash"] != hash:
#		logging.warning(
#			f"""Blurhashes for {restaurant['name']}, {restaurant['city']} don't match.
#			Stored blurhash: {restaurant['blurhash']}\nEncoded blurhash: {hash}"""
#			)


def get_valid_restaurants(restaurants: List[dict],
							query: str,
							lat: float,
							lon: float) -> List[dict]:
	""" Get list of restaurants that match the search distance and query """
	valid_restaurants = []

	for restaurant in restaurants:
		try:
			if check_distance(restaurant["location"], lat, lon) and\
				check_query(restaurant, query):
				validate_blurhash(restaurant)
				valid_restaurants.append(restaurant)
		except:
			logging.exception(f"Checking location and query string: {restaurant}")

	return valid_restaurants

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/restaurants/search", methods=["GET", "POST"])
def restaurant_search():
	try: # Validating input data
		if request.method == "GET":
			data = request.args
		else:
			data = request.form
		query = str(data.get("q"))
		lat = float(data.get("lat"))
		lon = float(data.get("lon"))
	except:
		logging.exception(f"Invalid query: {data}")
		return jsonify("Invalid input")
	
	if len(query) < QUERY_MIN_LENGTH:
		return jsonify(
			f"Search query too short (minimum {QUERY_MIN_LENGTH} character{int(bool(QUERY_MIN_LENGTH - 1)) * 's'})"
			)

	# No DB allowed per the assignment
	try:
		with open ("restaurants.json") as f:
			restaurants_list = json.load(f)["restaurants"]
	except:
		logging.exception("Couldn't get restaurants:")
		return jsonify("Couldn't get restaurants")

	restaurants = get_valid_restaurants(restaurants_list, query, lat, lon)

	return jsonify(restaurants)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
