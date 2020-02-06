/*
** Giant class for displaying a single restaurant's data
*/
class Restaurant extends React.Component {
	render() {
		const classnames = this.props.online ? "restaurant" : ("restaurant offline");
		const delivery_price = delivery_price_to_str(this.props.delivery_price, this.props.currency);
		return (
			<div className={classnames}>
				<img className="thumbnail" src={this.props.image}></img>
				<div className="restaurant_data_container">
					<div className="restaurant_data">
						<div className="restaurant_name">{this.props.name}</div>
						<div className="restaurant_info">
								<div className="restaurant_description">{this.props.description}</div>
								<div className="delivery_price">Delivery: {delivery_price}</div>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

class Sorting_Method extends React.Component {
	render () {
		return (
			<option>{this.props.name}</option>
		)
	}
}

/*
** Block for display of sorting and offline toggle options
*/
class Options extends React.Component {
	render() {
		let sorting_methods_rendered = [];
		for (let sorting_method of sorting_methods) {
			sorting_methods_rendered.push(
				React.createElement(Sorting_Method, sorting_method)
			);
		}

		return (
			<React.Fragment>
				<div id="sorting">
					Sort by:
					<select id="sort_by" defaultValue={sorting_methods[0].name}>
						{sorting_methods_rendered}
					</select>
				</div>
				<div id="offline_filter">
					<input type="checkbox" id="offline_checkbox"/>
					<label for="offline_checkbox">
						Only show restaurants that currently accept orders
					</label>
				</div>
			</React.Fragment>
		);
	}
}