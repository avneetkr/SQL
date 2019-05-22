'''
Problem#1

Print out a histogram of MPI National i.e. 
the number of countries that have MPI National 
in each of the following ranges: 
0.0-0.1, 0.1-0.2, 0.2-0.3, ..., 0.9-1.0. 
In each range, the lower bound is included, 
but not the upper bound, except for the last one.

Example output (there should be 10 lines at most) shown below. 
Each line prints the range lower bound and the count.

...
(0.6, <frequency>)
...
(0.3, <frequency>)
'''

def getLowerBound(value):

	if value>=0.0 and value<0.1:
		return 0.0

	elif value<0.2:
		return 0.1

	elif value<0.3:
		return 0.2

	elif value<0.4:
		return 0.3

	elif value<0.5:
		return 0.4

	elif value<0.6:
		return 0.5

	elif value<0.7:
		return 0.6

	elif value<0.8:
		return 0.7

	elif value<0.9:
		return 0.8

	elif value<=1.0:
		return 0.9

	else:
		return -1


def mapper (key, val):
	'''
	key: str, is the country code- ISO
    val: dict, dictionary of information about the country

    Return type is a list of (key, value) tuples. 
    '''
	s = []

	try:
		subnational = val['subnational']
		mpi_national = subnational[0]['MPI National']
		mpi_national_float = float(mpi_national)
		result = getLowerBound(mpi_national_float)
		s.append((result, 1))

	except:
		#Country does not have a subnational region
		pass

	

	return s


