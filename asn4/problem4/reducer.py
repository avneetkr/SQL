def reducer (key, list_of_vals):
	sum_urban = 0.0
	sum_rural = 0.0
	for val in list_of_vals:
		sum_urban = sum_urban + float(val[0]) # val[0]- mpi urban
		sum_rural = sum_rural + float(val[1]) # val[1]- mpi rural

	avg_urban = sum_urban/len(list_of_vals)
	avg_rural = sum_rural/len(list_of_vals)

	return [(key, ("%.3f" % avg_urban), ("%.3f" % avg_rural))]