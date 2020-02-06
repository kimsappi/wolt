const sorting_method_classes = {
	ALPHA: 1,
	DELIVERY_PRICE: 2
}

/*
**	name: Name of sorting method
**	class: Sorting basis (see const sorting_method_classes)
**	ascending: If this method should sort objects in ascending order, set to true
*/
const sorting_methods = [
	{
		name: "Name A-Z",
		class: sorting_method_classes.ALPHA,
		ascending: true
	},
	{
		name: "Name Z-A",
		class: sorting_method_classes.ALPHA,
		ascending: false
	},
	{
		name: "Delivery price (0-9)",
		class: sorting_method_classes.DELIVERY_PRICE,
		ascending: true
	},
	{
		name: "Delivery price (9-0)",
		class: sorting_method_classes.DELIVERY_PRICE,
		ascending: false
	}
]