def reducer (key, list_of_vals):
	#max_val- the pair (country name,value) with the max value
	max_val = list_of_vals[0]
	for val in list_of_vals:
		if float(val[1]) > float(max_val[1]): # val[0]: country name, val[1]:value
			max_val = val
	return [(key, max_val)]