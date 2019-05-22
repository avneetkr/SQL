'''
Problem#5

List the country and the sub-national region 
on the Pareto frontier of subnational headcount ratio 
and subnational deprivation intensity. 
For both headcount ratio and deprivation intensity, 
use the ranges: 0-10, 10-20, ..., 90-100.

Output example

...
((H, 30), (<country name>, 
			<subnational region name>, 
			<subnational region deprivation intensity>))
...
((I, 20), (<country name>, 
		   <subnational region name>, 
		   <subnational region headcount ratio>))
...

'''

def getLowerBound(value):

	if value>=0 and value<10:
		return 0

	elif value<20:
		return 10

	elif value<30:
		return 20

	elif value<40:
		return 30

	elif value<50:
		return 40

	elif value<60:
		return 50

	elif value<70:
		return 60

	elif value<80:
		return 70

	elif value<90:
		return 80

	elif value<=100:
		return 90

	else:
		return -1

def mapper (key, val):
	'''
	key: str, is the country code- ISO
    val: dict, dictionary of information about the country

    Returns: 
    list of 
    (('H', lower bound), (<country name>, 
			<subnational region name>, 
			<subnational region deprivation intensity>)).
     ('I', lower bound), (<country name>, 
		   <subnational region name>, 
		   <subnational region headcount ratio>))
	for all subnational regions
    '''
	s = []

	try:
		subnational = val['subnational']
		for region in subnational:
			hCount = region['Headcount Ratio Regional']
			hLowerBound = getLowerBound(float(hCount))

			iCount = region['Intensity of deprivation Regional']
			iLowerBound = getLowerBound(float(iCount))

			s.append((  ('H', hLowerBound) 
					  	,(  val['Country']
					       ,region['Sub-national region']
					       ,iCount) ))

			s.append(( ('I', iLowerBound)
				    , (  val['Country']
				    	,region['Sub-national region']
				    	,hCount) ))

	except:
		pass

	return s


