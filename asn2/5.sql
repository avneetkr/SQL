-- Problem 5
-- Output a table having columns World Region, Average MPI Urban,
-- Average MPI Rural. This table has one row for each world Region.
-- The Average MPI Urban column gives the Average urban MPI of countries
-- that have at least one sub-national region belonging to the corresponding
-- world region. The definition of Average MPI Rural is analogous
select World_region, avg(DISTINCT MPI_Urban), avg(DISTINCT MPI_rural)
from MPI_national, MPI_subnational
where MPI_national.Country = MPI_subnational.Country
group by World_region;
