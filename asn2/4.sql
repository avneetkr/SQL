--Problem 4
--Output a table having columns World Region, Average MPI National.
--This table has one row for each world region. The Average MPI National column 
--gives the average national MPI of countries that have at least one sub-national 
--region belonging to the corresponding world region.
select World_region, avg(MPI_National)
from MPI_subnational
group by World_region
having count(Sub_national_region) >= 1; 