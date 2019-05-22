--Problem 3
--Output a table having columns Country, MPI Urban, MPI Rural, 
--MPI National where MPI Urban >= 0.1, MPI Rural >= 0.2, MPI National is not null. 
--The countries should be sorted by MPI National in ascending order.
SELECT distinct MPI_subnational.Country, MPI_Urban, MPI_rural, MPI_National 
FROM MPI_national, MPI_subnational
WHERE MPI_national.Country = MPI_subnational.Country
AND (MPI_Urban >= 0.1 and MPI_rural >= 0.2)
AND (MPI_National is not null)
order by MPI_National; --ascending by default