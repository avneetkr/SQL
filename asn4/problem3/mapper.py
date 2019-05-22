'''
For the output, each row in the SQL output is
a tuple in our case. Each column in the SQL 
output is a field of the tuple in our case.

Problem #3:
with countries as (
select distinct 'World Region', 'Country', 'MPI National'
from MPI_subnational)
select 'World Region', avg('MPI National')
from countries
group by 'World Region';
'''
'''
World Region- is key from mapper
avg(MPI national)- do this in reducer
distinct world Region, country, mpi national- 
'''

def mapper (key, val):
	s = []
	count = {
	'Sub-Saharan Africa': 0
	,'Latin America and Caribbean': 0
	,'East Asia and the Pacific': 0
	, 'Arab States': 0
	, 'South Asia': 0
	, 'Europe and Central Asia': 0
	}

	try:
		country = val['Country']
		subnational = val['subnational']
		national = subnational[0]['MPI National']
		for region in subnational:
			world = region['World region']
			if count[world] == 0:
				s.append((world, national))
				count[world] = 1
	except:
		pass

	return s
