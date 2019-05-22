CREATE TABLE MPI_national (
ISO CHAR(3) NOT NULL PRIMARY KEY,
Country VARCHAR(100) NOT NULL,
[MPI Urban] REAL CHECK ([MPI Urban]>=0 AND [MPI Urban]<=1),
[Headcount Ratio Urban] REAL CHECK ([Headcount Ratio Urban]>=0 and [Headcount Ratio Urban]<=100),
[Intensity of Deprivation Urban] REAL CHECK ([Intensity of Deprivation Urban]>0 and [Intensity of Deprivation Urban]<=100),
[MPI Rural] REAL CHECK ([MPI Rural]>=0 AND [MPI Rural]<=1),
[Headcount Ratio Rural] REAL CHECK ([Headcount Ratio Rural]>=0 and [Headcount Ratio Rural]<=100),
[Intensity of Deprivation Rural] REAL CHECK ([Intensity of Deprivation Rural]>=0 and [Intensity of Deprivation Rural]<=100)
);

CREATE TABLE MPI_subnational (
[ISO country code] CHAR(3),
Country VARCHAR(100),
[Sub-national region] VARCHAR(100) NOT NULL,
[World region] VARCHAR(100) CHECK( [World region] IN ('Sub-Saharan Africa', 'Latin America and Caribbean', 'East Asia and the Pacific', 'Arab States', 'South Asia', 'Europe and Central Asia')) NOT NULL,
[MPI National] REAL CHECK ([MPI National]>=0 AND [MPI National]<=1),
[MPI Regional] REAL CHECK ([MPI Regional]>=0 AND [MPI Regional]<=1),
[Headcount Ratio Regional] REAL CHECK ([Headcount Ratio Regional]>=0 and [Headcount Ratio Regional]<=100),
[Intensity of deprivation Regional] REAL CHECK ([Intensity of deprivation Regional]>=0 and [Intensity of deprivation Regional]<=100),
CONSTRAINT Subnational PRIMARY KEY ([ISO Country code], [Sub-national region]),
FOREIGN KEY([ISO country code]) REFERENCES MPI_national(ISO),
FOREIGN KEY(Country) REFERENCES MPI_national(Country)
);
