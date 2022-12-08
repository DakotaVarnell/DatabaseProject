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
Movie_Title_ID	VARCHAR2(40) CONSTRAINT Movie_Movie_Title_Id_PK PRIMARY KEY, 
Movie_Name	VARCHAR2(40),
Popularity NUMBER(38),
IMDB_Rating FLOAT(40),
Certification VARCHAR2(20),
Box_Office_Revenue NUMBER(25),
Budget NUMBER(25)
);

CREATE TABLE Directs(
dName VARCHAR2(40) CONSTRAINT Directs_dName_uk UNIQUE,
Movie_Title_Id VARCHAR2(25)
);

CREATE TABLE Writes(
wName VARCHAR2(40) CONSTRAINT Writes_wName_uk UNIQUE,
Movie_Title_Id VARCHAR2(25)
);

CREATE TABLE Contains(
Soundtrack_Title VARCHAR2(100),
Movie_Title_Id VARCHAR2(25),
CONSTRAINT Contains_Title_PK PRIMARY KEY(Soundtrack_Title,Movie_Title_Id)
);

CREATE TABLE Reviews(
Username VARCHAR2(40),
Review_Contents VARCHAR2(3000),
Score VARCHAR2(40), 
Date_of_Review DATE,
Rev_Movie_Id VARCHAR2(40),
CONSTRAINT Reviews_Username_PK PRIMARY KEY(Username,Rev_Movie_Id)
);

CREATE TABLE Genres(
Genre VARCHAR2(40),
Movie_Title_Id VARCHAR2(25),
CONSTRAINT Genres_Genre_PK PRIMARY KEY(Genre,Movie_Title_Id)
);

CREATE TABLE Languages(
Lang VARCHAR2(40),
Movie_Title_Id VARCHAR2(25),
CONSTRAINT Languages_Lang_PK PRIMARY KEY(Lang,Movie_Title_Id)
);

CREATE TABLE Award(
ID	VARCHAR2(25), 
Award_Name	VARCHAR2(40),
Date_of_Award NUMBER(20),
Result VARCHAR2(40),
Award_Event VARCHAR2(200),
Award_Type VARCHAR2(200),
CONSTRAINT Award_ID_PK PRIMARY KEY(ID, Award_Name, Award_Type)
);

CREATE TABLE Person(
Name    VARCHAR2(70) CONSTRAINT Person_Name_PK PRIMARY KEY,
Birthdate VARCHAR2(40),
Hometown VARCHAR2(70),
Number_Of_Movies NUMBER(38),
Actor_Flag VARCHAR2(1),
Writer_Flag VARCHAR2(1),
Director_Flag VARCHAR2(1)
);

CREATE TABLE Soundtrack(
Title	VARCHAR2(100) CONSTRAINT Soundtrack_Title_PK PRIMARY KEY,
Song_Title VARCHAR(70),
Writer_Name VARCHAR(70),
Performer_Name VARCHAR2(70)
);

CREATE TABLE Works_For(
Movie_Title_ID	VARCHAR2(20), 
aName VARCHAR2(70) CONSTRAINT Works_For_aName_uk UNIQUE,
Pay VARCHAR(100)
);

ALTER TABLE Directs
    ADD CONSTRAINT Directs_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Writes
    ADD CONSTRAINT Writes_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Contains
    ADD CONSTRAINT Contains_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Contains
    ADD CONSTRAINT Contains_Soundtrack_Title_fk FOREIGN KEY(Soundtrack_Title)
    REFERENCES Soundtrack(Title);

ALTER TABLE Reviews
    ADD CONSTRAINT Reviews_Rev_Movie_Id_fk FOREIGN KEY(Rev_Movie_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Genres
    ADD CONSTRAINT Genres_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Languages
    ADD CONSTRAINT Languages_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Award
    ADD CONSTRAINT Award_ID_fk FOREIGN KEY(ID)
    REFERENCES Movie(Movie_Title_Id);


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
