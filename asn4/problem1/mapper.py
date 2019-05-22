'''
For the output, each row in the SQL output is
a tuple in our case. Each column in the SQL 
output is a field of the tuple in our case.

Problem #1:
select 'Country', 'MPI Urban', 'MPI Rural'
from MPI_national
where 'MPI Urban' >= 0.1 and 'MPI Rural' >= 0.2;
'''

def mapper (key, val):
	s = []

	try:
		country = val['Country']
		urban = val['MPI Urban']
		rural = val['MPI Rural']

		if float(urban) >= 0.1 and float(rural) >=0.2:
			s.append((key, (country, urban, rural)))
	except:
		pass

	return s
