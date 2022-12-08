--Where our Queries will go

--1 Design 1 meaningful query use only one table
--Get all movies with the highest ratings
SELECT * from movie where rating > 9;

--2 Design 2 meaningful queries that join two tables
SELECT Movie.Movie_Name, Writes.wName
FROM Movie
INNER JOIN Writes ON Movie.Movie_Title_Id=Writes.Movie_Title_Id;

--3 Design 2 meaningful queries that join two tables


--4 Design 2 meaningful queries that join three tables

--5 Design 2 meaningful queries that join three tables

--6 Design 1 meaningful query that joins four tables

--7 Design 2 meaningful queries that use set theory (union, intersection or minus) operations
SELECT dName FROM Directs WHERE Movie_Title_Id='0068646'
UNION
SELECT wName FROM Writes WHERE Movie_Title_Id='0068646';

--8 Design 2 meaningful queries that use set theory (union, intersection or minus) operations
SELECT wName FROM Writes
INTERSECT
SELECT dName from Directs;

--9 Design 2 meaningful queries that use grouping operations
SELECT COUNT(Movie_Title_Id) from Movie;

--10 Design 2 meaningful queries that use grouping operations
SELECT AVG(budget) FROM movies;
