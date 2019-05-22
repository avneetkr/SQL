'''
Problem#4

List the average MPI subnational for each world region.

Output example (there should be one line for each world region in this format)

(<world region name>, <average MPI subnational>)

'''

def mapper (key, val):
	'''
	key: str, is the country code- ISO
    val: dict, dictionary of information about the country

    Returns: 
    [(('H', lower bound), (country name, intensity)).
     ('I', lower bound), (country name, headcount))]
    '''
	s = []

	try:
		subnational = val['subnational']
		for region in subnational:
			s.append((region['World region'], region['MPI Regional']))
	except:
		pass

	return s


