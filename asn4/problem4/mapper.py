'''
For the output, each row in the SQL output is
a tuple in our case. Each column in the SQL 
output is a field of the tuple in our case.

Problem #4:
with regions as (
select distinct 'World Region', 'Country'
from MPI_subnational)
select 'World Region', avg('MPI Urban'), avg('MPI Rural')
from regions join MPI_national using ('Country')
group by  'World Region';

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
		urban = val['MPI Urban']
		rural = val['MPI Rural']
		subnational = val['subnational']
		for region in subnational:
			world = region['World region']
			if count[world] == 0:
				s.append((world, (urban, rural)))
				count[world] = 1
	except:
		pass

	return s
