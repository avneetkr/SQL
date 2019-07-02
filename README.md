# SQL & MapReduce
This repository contains python code to
1. Create tables MPI_National and MPI_subnational with ERD constraints and Foreign Keys

2. SQL queries to 
	1. Output a table having columns Country, MPI Urban, MPI Rural where MPI Urban>=0.1 and MPI Rural >=0.2
	2. Output a table having columns Country, MPI Urban, MPI Rural, MPI National. Do not include countries whose MPI National value is unknown.
	3. Output a table having columns Country, MPI Urban, MPI Rural, MPI National where MPI Urban >= 0.1, MPI Rural >= 0.2, MPI National is not null. The countries should be sorted by MPI National in ascending order.
	4. Output a table having columns World Region, Average MPI National.This table has one row for each world region. The Average MPI National column gives the average national MPI of countries that have at least one sub-national region belonging to the corresponding world region.
	5. Output a table having columns World Region, Average MPI Urban, Average MPI Rural. This table has one row for each world Region. The Average MPI Urban column gives the Average urban MPI of countries that have at least one sub-national region belonging to the corresponding world region.

3. Mapper & Reducer methods to
   1. Print out a histogram of MPI National i.e. 
      the number of countries that have MPI National 
      in each of the following ranges: 
      0.0-0.1, 0.1-0.2, 0.2-0.3, ..., 0.9-1.0. 
      In each range, the lower bound is included, 
      but not the upper bound, except for the last one.

      Example output (there should be 10 lines at most) shown below. 
      Each line prints the range lower bound and the count.
			
			(0.6, frequency)
			(0.3, frequency)
      
    2. Do the same as problem #1, except add a line for countries whose MPI National is unknown. Represent the line as:
				
				(-1, frequency)
       
    3. Urban poverty index depends both on urban headcount ratio and urban intensity of deprivation. I want to list the countries that are on the Pareto frontier of these two parameters. A country is on the Pareto frontier if:
				it has the maximum intensity of deprivation in a given range of headcount ratio, or,
				it has the maximum headcount ratio for a given range of deprivation intensity.
				For both headcount ratio and deprivation intensity, use the ranges: 0-10, 10-20, ..., 90-100.
				The output looks like ((bin type, bin lower bound), value)
				
				((H, 30), (country name, urban deprivation intensity))
				((I, 20), (country name, urban headcount ratio))
      
   4. List the average MPI subnational for each world region.Output example (there should be one line for each world region in this format)
	 		
			(world region name, average MPI subnational)
      
   5. List the country and the sub-national region 
      on the Pareto frontier of subnational headcount ratio 
      and subnational deprivation intensity. 
      For both headcount ratio and deprivation intensity, 
      use the ranges: 0-10, 10-20, ..., 90-100.

      Output example

      	((H, 30), (country name, subnational region name, subnational region deprivation intensity))
      
      
4. Convert the following SQL queries to MapReduce
   1. select 'Country', 'MPI Urban', 'MPI Rural'
      from MPI_national
      where 'MPI Urban' >= 0.1 and 'MPI Rural' >= 0.2;
   2. select distinct 'Country', 'MPI Urban', 'MPI Rural', 'MPI National'
      from 
      MPI_national join MPI_subnational 
      using ('Country');
      
   3. with countries as (
      select distinct 'World Region', 'Country', 'MPI National'
      from MPI_subnational)
      select 'World Region', avg('MPI National')
      from countries
      group by 'World Region';
      
   4. with regions as (
      select distinct 'World Region', 'Country'
      from MPI_subnational)
      select 'World Region', avg('MPI Urban'), avg('MPI Rural')
      from regions join MPI_national using ('Country')
      group by  'World Region';
