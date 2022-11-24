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
Movie_Title_ID	VARCHAR2(20) CONSTRAINT Movie_Movie_Title_Id_PK PRIMARY KEY, 
Movie_Name	VARCHAR2(20),
Popularity NUMBER(15),
IMDB_Rating NUMBER(3),
Certification VARCHAR2(20),
Box_Office_Revenue NUMBER(15),
Budget NUMBER(10)
);

CREATE TABLE Directs(
dName VARCHAR2(40) CONSTRAINT Directs_dName_uk UNIQUE,
Movie_Title_Id VARCHAR2(20)
);

CREATE TABLE Writes(
wName VARCHAR2(40) CONSTRAINT Writes_wName_uk UNIQUE,
Movie_Title_Id VARCHAR2(20)
);

CREATE TABLE Contains(
Soundtrack_Title VARCHAR2(30),
Movie_Title_Id VARCHAR2(20),
CONSTRAINT Contains_Soundtrack_Title_PK PRIMARY KEY(Soundtrack_Title,Movie_Title_Id)
);

CREATE TABLE Reviews(
Username VARCHAR2(25),
Review_Contents VARCHAR2(100),
Score VARCHAR2(20), 
Date_of_Review DATE,
Rev_Movie_Id VARCHAR2(20),
CONSTRAINT Reviews_Username_PK PRIMARY KEY(Username,Rev_Movie_Id)
);

CREATE TABLE Genres(
Genre VARCHAR2(20),
Movie_Title_Id VARCHAR2(20),
CONSTRAINT Genres_Genre_PK PRIMARY KEY(Genre,Movie_Title_Id)
);

CREATE TABLE Languages(
Lang VARCHAR2(20),
Movie_Title_Id VARCHAR2(20),
CONSTRAINT Languages_Lang_PK PRIMARY KEY(Lang,Movie_Title_Id)
);

CREATE TABLE Award(
ID	VARCHAR2(20) CONSTRAINT Award_ID_PK PRIMARY KEY, 
Award_Name	VARCHAR2(20),
Date_of_Award DATE,
Award_Event VARCHAR2(20),
Movie_Receives VARCHAR2(20),
Actor_Receives VARCHAR2(20),
Writer_Receives VARCHAR2(20),
Director_Receives VARCHAR2(20)
);

CREATE TABLE Person(
Name    VARCHAR(40) CONSTRAINT Person_Name_PK PRIMARY KEY,
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
Title	VARCHAR2(25) CONSTRAINT Soundtrack_Title_PK PRIMARY KEY,
cName VARCHAR(20),
Performer_FName VARCHAR2(20),
Performer_LName VARCHAR2(20),
Ratings NUMBER(20)
);

CREATE TABLE Works_For(
Movie_Title_ID	VARCHAR2(20), 
aName VARCHAR2(40) CONSTRAINT Works_For_aName_uk UNIQUE,
Supporting VARCHAR2(20),
Leading VARCHAR2(20),
Pay NUMBER(20)
);

ALTER TABLE Directs
    ADD CONSTRAINT Directs_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Writes
    ADD CONSTRAINT Writes_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_Id)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Works_For
    ADD CONSTRAINT Works_For_Movie_Title_Id_fk FOREIGN KEY(Movie_Title_ID)
    REFERENCES Movie(Movie_Title_Id);

ALTER TABLE Directs
    ADD CONSTRAINT Directs_dName_fk FOREIGN KEY(dName)
    REFERENCES Person(Name);

ALTER TABLE Writes
    ADD CONSTRAINT Writes_wName_fk FOREIGN KEY(wName)
    REFERENCES Person(Name);

ALTER TABLE Works_For
    ADD CONSTRAINT Works_For_aName_fk FOREIGN KEY(aName)
    REFERENCES Person(Name);

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
    ADD CONSTRAINT Award_Movie_Receives_fk FOREIGN KEY(Movie_Receives)
    REFERENCES Movie(Movie_Title_Id);
ALTER TABLE Award
    ADD CONSTRAINT Award_Actor_Receives_fk FOREIGN KEY(Actor_Receives)
    REFERENCES Works_For(aName);
ALTER TABLE Award
    ADD CONSTRAINT Award_Director_Receives_fk FOREIGN KEY(Director_Receives)
    REFERENCES Directs(dName);
ALTER TABLE Award
    ADD CONSTRAINT Award_Writer_Receives_fk FOREIGN KEY(Writer_Receives)
    REFERENCES Writes(wName);

ALTER TABLE Works_For
    ADD CONSTRAINT Works_For_aName_PK PRIMARY KEY(aName,Movie_Title_ID);

ALTER TABLE Directs
    ADD CONSTRAINT Directs_dName_PK PRIMARY KEY(dName,Movie_Title_Id);

ALTER TABLE Writes
    ADD CONSTRAINT Writes_wName_PK PRIMARY KEY(wName,Movie_Title_Id);

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