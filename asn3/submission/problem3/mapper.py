'''
Problem#3

Urban poverty index depends both on urban headcount ratio 
and urban intensity of deprivation. 
I want to list the countries that are on the 
Pareto frontier of these two parameters. 

A country is on the Pareto frontier if:

it has the maximum intensity of deprivation in a given range of headcount ratio, or,
it has the maximum headcount ratio for a given range of deprivation intensity.

For both headcount ratio and deprivation intensity, 
use the ranges: 0-10, 10-20, ..., 90-100.

The output looks like ((bin type, bin lower bound), value)

...
((H, 30), (<country name>, <urban deprivation intensity>))
...
((I, 20), (<country name>, <urban headcount ratio>))
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
    [(('H', lower bound), (country name, intensity)).
     ('I', lower bound), (country name, headcount))]
    '''
	s = []

	try:
		hCount = val['Headcount Ratio Urban']
		hLowerBound = getLowerBound(float(hCount))

		iCount = val['Intensity of Deprivation Urban']
		iLowerBound = getLowerBound(float(iCount))

		s = [ ( ('H', hLowerBound), (val['Country'],iCount) )
			 ,( ('I', iLowerBound), (val['Country'], hCount) ) ]

	except:
		pass

	return s


