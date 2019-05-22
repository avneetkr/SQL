'''
For the output, each row in the SQL output is
a tuple in our case. Each column in the SQL 
output is a field of the tuple in our case.

Problem #2:
select distinct 'Country', 'MPI Urban', 'MPI Rural', 'MPI National'
from 
MPI_national join MPI_subnational 
using ('Country');
'''

def mapper (key, val):
	s = []

	try:
		country = val['Country']
		urban = val['MPI Urban']
		rural = val['MPI Rural']	
		national = val['subnational'][0]['MPI National']

		s.append((key, (country, urban, rural, national)))

	except:
		pass

	return s
