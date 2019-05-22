def reducer (key, list_of_vals):
	float_list_of_vals = [float(i) for i in list_of_vals]
	sum_of_vals = sum(float_list_of_vals)
	result = sum_of_vals/len(list_of_vals)

	return [(key, "%.3f" % result)]