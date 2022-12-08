--Where our Queries will go

--1 Design a meaningful query use only one table
--Get all movies with the highest ratings
SELECT * from movie where rating > 9;

--2 Design a meaningful queries that join two tables
SELECT Movie.Movie_Name, Writes.wName
FROM Movie
INNER JOIN Writes ON Movie.Movie_Title_Id=Writes.Movie_Title_Id;

--3 Design a meaningful queries that join two tables
SELECT Movie.Movie_Title_Id,Movie.Movie_Name, Reviews.Score
FROM Movie
INNER JOIN Reviews ON Movie.Movie_Title_Id=Reviews.Rev_Movie_Id;

--4 Design a meaningful queries that join three tables

--5 Design a meaningful queries that join three tables
SELECT Name, Genre, Lang
FROM Genres NATURAL JOIN Movie Natural Join Languages
WHERE Genre='Drama' and Lang='Mandarin';

--6 Design a meaningful query that joins four tables
SELECT Name, Number_Of_Movies, Genre
FROM Genres NATURAL JOIN Movie NATURAL JOIN Works_For NATURAL JOIN Person
WHERE Genre='Action' and Number_Of_Movies=45;

--7 Design a meaningful queries that use set theory (union, intersection or minus) operations
SELECT dName FROM Directs WHERE Movie_Title_Id='0068646'
UNION
SELECT wName FROM Writes WHERE Movie_Title_Id='0068646';

--8 Design a meaningful queries that use set theory (union, intersection or minus) operations
SELECT wName FROM Writes
INTERSECT
SELECT dName from Directs;

--9 Design a meaningful queries that use grouping operations
SELECT COUNT(Movie_Title_Id) from Movie;

--10 Design a meaningful queries that use grouping operations
SELECT AVG(budget) FROM Movie;
