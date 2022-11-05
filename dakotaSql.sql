DROP TABLE Movie CASCADE CONSTRAINTS;
DROP TABLE Directs CASCADE CONSTRAINTS;
DROP TABLE Writes CASCADE CONSTRAINTS;
DROP TABLE Contains CASCADE CONSTRAINTS;
DROP TABLE Reviews CASCADE CONSTRAINTS;
DROP TABLE Genres CASCADE CONSTRAINTS;
DROP TABLE Languages CASCADE CONSTRAINTS;
DROP TABLE Award CASCADE CONSTRAINTS;
DROP TABLE Person CASCADE CONSTRAINTS;
DROP TABLE Soundtrack CASCADE CONSTRAINTS;
DROP TABLE Works_For CASCADE CONSTRAINTS;


CREATE TABLE Movie(
Movie_Title_ID	VARCHAR2(20), 
Movie_Name	VARCHAR2(20),
Popularity NUMBER(15),
IMDB_Rating NUMBER(3),
Certification VARCHAR2(20),
Box_Office_Revenue NUMBER(15),
Budget NUMBER(10),
Writer_FName VARCHAR2(20),
Writer_LName VARCHAR(20)
);

CREATE TABLE Directs(
Director_FName VARCHAR2(20),
Director_LName VARCHAR2(20),
Movie_Title_Id_Direct VARCHAR2(20)
);

CREATE TABLE Writes(
WriterFName VARCHAR2(20),
Writer_LName VARCHAR2(20),
Movie_Title_Id_Writer VARCHAR2(20)
);

CREATE TABLE Contains(
Soundtrack_Title VARCHAR2(30),
Movie_Title_Id_Contain VARCHAR2(20)
);

CREATE TABLE Reviews(
Username VARCHAR2(25),
Review_Contents VARCHAR2(100),
Score VARCHAR2(20), 
Date_of_Review DATE,
Rev_Movie_Id VARCHAR2(20)
);

CREATE TABLE Genres(
Genre VARCHAR2(20),
Movie_Title_Id_Genre VARCHAR2(20)
);

CREATE TABLE Languages(
Lang VARCHAR2(20),
Movie_Title_Id_Languages VARCHAR2(20)
);

CREATE TABLE Award(
ID	VARCHAR2(20), 
Award_Name	VARCHAR2(20),
Recipient_FName VARCHAR2(20),
Recipient_LName VARCHAR2(20),
Date_of_Award DATE,
Award_Event VARCHAR2(20),
Movie_Receives VARCHAR2(20),
Actor_Receives VARCHAR2(20),
Writer_Receives VARCHAR2(20),
Director_Receives VARCHAR2(20)
);

CREATE TABLE Person(
First_Name	VARCHAR2(20), 
Last_Name	VARCHAR2(20),
Birthdate DATE,
Hometown VARCHAR2(25),
Gender VARCHAR2(20),
Spouse_FName VARCHAR2(25),
Spouse_LName VARCHAR2(25),
Parents_FName VARCHAR2(25),
Parents_LName VARCHAR2(25),
Children_FName VARCHAR2(25),
Children_LName VARCHAR2(25),
Number_Of_Movies NUMBER(20),
Actor_Flag VARCHAR2(20),
Writer_Flag VARCHAR2(20),
Director_Flag VARCHAR2(20)
);

CREATE TABLE Soundtrack(
Title	VARCHAR2(25), 
Writer_FName VARCHAR2(20),
Writer_LName VARCHAR2(20),
Performer_FName VARCHAR2(20),
Performer_LName VARCHAR2(20),
Ratings NUMBER(20)
);

CREATE TABLE Works_For(
Movie_Title_ID_WorksFor	VARCHAR2(20), 
Actor_FName VARCHAR2(20),
Actor_LName VARCHAR2(20),
Supporting VARCHAR2(20),
Leading VARCHAR2(20),
Pay NUMBER(20)
);


-- INSERT INTO Movie
-- VALUES('12345','Lion King', 1500, 5, 'PG-13', 200000, 100000, 'Guillermo', 'DelTorro'); 

-- INSERT INTO Movie
-- VALUES('12222','The Little Mermaid', 1600, 6, 'PG-13', 300000, 100000, 'Michael', 'Tortoise'); 

-- INSERT INTO Movie
-- VALUES('15555','Tarzan', 1700, 7, 'PG-13', 400000, 100000, 'Thomas', 'Bay'); 

-- INSERT INTO Directs
-- VALUES('John', 'Smith','162jdjd7');

-- INSERT INTO Directs
-- VALUES('Tanner', 'Canada', '1332323jj');

-- INSERT INTO Directs
-- VALUES('Jack', 'White', '12121212dd');

-- ALTER TABLE Movie
-- ADD CONSTRAINT movie_movieTitleId_pk PRIMARY KEY(Movie_Title_Id);

-- ALTER TABLE Directs
-- ADD CONSTRAINT directs_MovieTableID_fk FOREIGN KEY(Movie_Title_Id_Direct)
-- REFERENCES Movie(Movie_Title_Id);


-- SELECT * FROM Movie;
-- SELECT * FROM Directs;
-- SELECT * FROM Writes;
-- SELECT * FROM Contains;
-- SELECT * FROM Reviews;
-- SELECT * FROM Genres;
-- SELECT * FROM Languages;
-- SELECT * FROM Award;
-- SELECT * FROM Person;
-- SELECT * FROM Soundtrack;
-- SELECT * FROM Works_For;

DESC Movie;
DESC Directs;
DESC Writes;
DESC Contains;
DESC Reviews;
DESC Genres;
DESC Languages;
DESC Award;
DESC Person;
DESC Soundtrack;
DESC Works_For;



