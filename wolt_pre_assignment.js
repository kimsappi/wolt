class Restaurant_Description {
	constructor(description) {
		return React.createElement(
			"em",
			{
				className: "description"
			},
			description
		);
	}
}

class Restaurant_Delivery_Price {
	constructor(price, currency) {
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
		}

		return React.createElement(
			"div",
			{
				className: "delivery_price"
			},
			"Delivery price: " + main_currency + '.' + fractional_currency + ' ' + currency
		);
	}
}

class Restaurant_Info {
	constructor(props) {
		return React.createElement(
			"div",
			{
				className: "restaurant_info"
			},
			new Restaurant_Description(props.description),
			new Restaurant_Delivery_Price(props.delivery_price, props.currency)
		);
	}
}

class Restaurant_Thumbnail {
	constructor(props) {
		return React.createElement(
			"img",
			{
				src: props.image,
				className: "thumbnail"
			}
		);
	}
}

class Restaurant_Name {
	constructor(props) {
		return React.createElement(
			"div",
			{
				className: "name"
			},
			props.name, new Restaurant_Info(props)
		);
	}
}

class Restaurant extends React.Component {
	render() {
		return React.createElement(
			"div",
			{
				className: "restaurant" + " online" + String(this.props.online),
				key: this.props.name.replace(/\s/g, "")
			},
			new Restaurant_Thumbnail(this.props),
			new Restaurant_Name(this.props)
		);
	}
}

function render_restaurants(restaurants) {
	let restaurants_rendered = [];
	for (let restaurant of restaurants) {
		restaurants_rendered.push(
			React.createElement(Restaurant, restaurant)
		);
	}
	ReactDOM.render(
		restaurants_rendered,
		$("#restaurants_flex")[0]
	);
}

window.onload = function () {
	$.getJSON("https://raw.githubusercontent.com/woltapp/summer2020/master/restaurants.json",
		function(data) {
			restaurants = data.restaurants;
			render_restaurants(restaurants);
		}
	);
};