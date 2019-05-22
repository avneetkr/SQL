def reducer (key, list_of_vals):
	#max_val- the pair (country name,value) with the max value
	max_val = list_of_vals[0]
	for val in list_of_vals:
		if float(val[2]) > float(max_val[2]): # val[0]: country name, val[1]: subnational region name, val[2]:value
			max_val = val
	return [(key, max_val)]