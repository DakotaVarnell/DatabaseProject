DROP TABLE Movie CASCADE CONSTRAINTS;
DROP TABLE Directs CASCADE CONSTRAINTS;


CREATE TABLE Movie(
Movie_Title_ID	VARCHAR2(20), 
Name	VARCHAR2(20),
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

INSERT INTO Movie
VALUES('12345','Lion King', 1500, 5, 'PG-13', 200000, 100000, 'Guillermo', 'DelTorro'); 

INSERT INTO Movie
VALUES('12222','The Little Mermaid', 1600, 6, 'PG-13', 300000, 100000, 'Michael', 'Tortoise'); 

INSERT INTO Movie
VALUES('15555','Tarzan', 1700, 7, 'PG-13', 400000, 100000, 'Thomas', 'Bay'); 

INSERT INTO Directs
VALUES('John', 'Smith','162jdjd7');

INSERT INTO Directs
VALUES('Tanner', 'Canada', '1332323jj');

INSERT INTO Directs
VALUES('Jack', 'White', '12121212dd');

ALTER TABLE Movie
ADD CONSTRAINT movie_movieTitleId_pk PRIMARY KEY(Movie_Title_Id);

ALTER TABLE Directs
ADD CONSTRAINT directs_MovieTableID_fk FOREIGN KEY(Movie_Title_Id_Direct)
REFERENCES Movie(Movie_Title_Id);


SELECT * FROM Movie;
SELECT * FROM Directs;


