--Problem 2
--Output a table having columns Country, MPI Urban, MPI Rural, MPI National. 
--Do not include countries whose MPI National value is unknown.
SELECT distinct MPI_national.Country, MPI_Urban, MPI_rural, MPI_National
FROM MPI_national, MPI_subnational
WHERE MPI_national.Country = MPI_subnational.Country
AND MPI_National is not NULL;

