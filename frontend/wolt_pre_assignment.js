function delivery_price_to_str(price, currency) {
	let decimal_separator = "."
	let main_currency = String(price).slice(0, -2);
	let fractional_currency = String(price).slice(-2);
	if (main_currency === "") {
		main_currency = "0";
	}
	if (fractional_currency.length === 1) {
		fractional_currency = "0" + fractional_currency;
	}

	if (currency === "EUR") {
		currency = "€";
		decimal_separator = ","
	}
	return main_currency + decimal_separator + fractional_currency + " " + currency
}

function render_restaurants() {
	const restaurants_rendered = [];
	for (const restaurant of window.restaurants) {
		restaurants_rendered.push(
			React.createElement(Restaurant, restaurant)
		);
	}
	ReactDOM.render(
		restaurants_rendered,
		$("#restaurants_flex")[0]
	);
}

/*
** Toggles display of offline restaurants.
*/
function filter_offline() {
	if ($("#offline_checkbox")[0].checked) {
		$(".offline").css("display", "none");
	}
	else {
		$(".offline").css("display", "block");
	}
}

function sort_restaurants() {
	let sort_by = $("#sort_by").find(":selected").text();
	let sort_by_object = null;

	for (let sorting_method of sorting_methods) {
		if (sort_by === sorting_method.name) {
			sort_by_object = sorting_method;
		}
	}
	if (sort_by_object != null) {
		// "Easily" extensible way to add more sorting methods.
		// Restaurants should be sorted in ascending order by default.
		switch(sort_by_object.class) {

			case sorting_method_classes.ALPHA:
				window.restaurants.sort((a, b) => (a.name > b.name) ? 1 : -1);
				break;

			case sorting_method_classes.DELIVERY_PRICE:
				window.restaurants.sort((a, b) => (a.delivery_price > b.delivery_price) ? 1 : -1);
				break;

		}
		// Restaurants should always be sorted in ascending order above,
		//	this will reverse them if order should be descending.
		if (!sort_by_object.ascending) {
			window.restaurants.reverse();
		}
	}
	render_restaurants();
}

function onload_init() {
	$.getJSON("https://raw.githubusercontent.com/woltapp/summer2020/master/restaurants.json")
		.done((data) => {
			window.restaurants = data.restaurants;
			sort_restaurants();
			render_restaurants();
		})
		.fail(() => {
			ReactDOM.render(
				<p>Couldn't load restaurant data</p>,
				$("#restaurants_flex")[0]
			)
		});

	// This isn't really required, but I wanted to explore React further
	// Renders the "Sort by" dropdown
	ReactDOM.render(
		<Options />,
		$("#options")[0]
	);
	$("#offline_checkbox")[0].addEventListener("change", filter_offline);
	$("#sort_by")[0].addEventListener("change", sort_restaurants);
};

$(document).ready(() => { onload_init(); });