--Problem 1
--Output a table having columns Country, MPI Urban, MPI Rural 
--where MPI Urban>=0.1 and MPI Rural >=0.2
SELECT Country, MPI_Urban, MPI_Rural 
FROM MPI_national
where MPI_Urban >= 0.1 and MPI_rural >= 0.2;