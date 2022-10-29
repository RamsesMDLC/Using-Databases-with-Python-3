# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:20:24 2020

@author: USUARIO
"""

#PART 1.1: I wil use "JSON" because I need to parse JSON text..
import json

#PART 1.2: Import the library of SQL lite Browser
import sqlite3

#PART 2: Making the connection between the Python File and...
#...the SQL Database. 
#The "Week4_Test1.sqlite" is the name of the SQL DataBase

#Extra 1= This API opens a connection to the SQLite database...
#...file
#Extra 2: sqlite3.connect(database [,timeout ,other optional arguments])
conn = sqlite3.connect("Week4_Test1.sqlite")

#PART 3: This code allow me to "File Handle"(i.e."Identificar Archivos")...
# Also allow the transmission of information. Specificalley...
#...it Open and Send SQL Commands  through the Cursor and then...
#... we read the Cursor and get response (i.e. "we get the data back")...
#...through the same Cursor.
#In addition, the Cursor is like the "File Handle"of the "Database Server".
#It is important to say that the "Connection" can create more than one...
#...Cursor.

#Extra 1= This routine creates a Cursor which will be used throughout..
#...of your database programming with Python

#Extra 2: connection.cursor([cursorClass])
cur = conn.cursor()

#PART 4.1: This code juste check if alredy exists any Table...
#... in SQLite3, called "User", "Member" and "Course"...
#...and if exist, it will be deleted. This is eith the code "DROP TABLE"

#PART 4.2.1: This code create Tables in SQLite3 called...
#..."User", "Member" and "Course" with the code "CREATE TABLE".
#It will also establish the "id", "name", "title" and "role" of...
#...every object per Table, respectively.
# Also Make some fresh tables using "executescript()"

#PART 4.2.2: This code allow me to write statements separates...
#... with semicoloin SQL Table trough Python.

#PART 4.2.3: The code "PRIMARY KEY (user_id, course_id)" behave like...
#..."Composite Primary Key", this "Composite Primary Key" is unique...
#...because represente thee unique combination of the "user_id" and...
#..."course_id"

#PART 4.2.4: The code "UNIQUE" allow me to use only one specific...
#...string. If we use or find that specific string again the program...
#...will probably send a error message. For example: the a specific...
#...string is a name of a student or a name of a professor.

#Extra 1= This routine executes multiple SQL statements at once provided...
#...in the form of script (The script form is inside of triple quotation...
#...mark """ """"). All the SQL statements should be separated by...
#...a semi colon (;).

#Extra 2: cursor.executescript(sql_script)

#Extra 3.1: NOT NULL is a constraint to ensure the values in a column...
#...are not NULL.

#Extra 3.2: When you create a table, you can specify whether a column...
#...acceptsNULL values or not. By default, all columns in a table...
#...accept NULL values except you explicitly use NOT NULL constraints.

#Extra 3.3: Based on the SQL standard, PRIMARY KEY should always...
#...imply NOT NULL. However, SQLite allows NULL values in the PRIMARY KEY...
#..,column except that a column is INTEGER PRIMARY KEY.

#Extra 4.1:PRIMARY KEY is a constraint to define a primary key for a table.

#Extra 4.2:A primary key is a column or group of columns used to...
#...identify the uniqueness of rows in a table. Each table has one and...
#...only one primary key.

#Extra 5.1:SQLite AUTOINCREMENT column is an attribute.

#Extra 5.2: Whenever you create a table without specifying the WITHOUT ID...
#...option, you get an implicit auto-increment column called ID. The...
#...ID column store 64-bit signed integer that uniquely identifies a...
#...row in the table.

#Extra 5.3: The AUTOINCREMENT keyword imposes extra CPU, memory...
#...disk space, and disk I/O overhead and should be avoided if not...
#...strictly needed. It is usually not needed.

#Extra 5.4: The main purpose of using attribute AUTOINCREMENT is...
#...to prevent SQLite to reuse a value that has not been used or a...
#...value from the previously deleted row.

#Extra 6.1: SQLite UNIQUE is a constraint to ensure all values in a...
#...column or a group of columns are unique.

#Extra 6.2: Once a UNIQUE constraint is defined, if you attempt to...
#...insert or update a value that already exists in the column,...
#...SQLite will issue an error and abort the operation.

#Extra 6.3: SQLite treats all NULL values are different, therefore,...
#...a column with a UNIQUE constraint can have multiple NULL values.

#Extra 7.1: The order of the code, for example in the Table "Member",...
#...the consequent order described in Python of "user_id", "course_id"...
#..."role" and "PRIMARY KEY" is reflected in how these columns appears...
#...in the Database. 

cur.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
""")

#PART 5: In this part, the Python File will prompt for the...
#...the name of File in format JSON
fname = input("Enter file name: ")

#PART 6: Open the File
str_data = open(fname).read()

#PART 7: Parsing the JSON
json_data = json.loads(str_data)

#PART 8: In this part we will apply a Loop through every line...
#... of the JSON file to complete the Database with the...
#...information of "User", "Member" and "Course".
for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]

    print((name, title, role))

#PART 9.1: In this part we will select every piece of data that we found...
# in the File in format JSON through the Python Code and then...
#...introduce them in the SQL Database. Specifically, this...
#...code is opening the record set in the SQL Database.

#PART 9.2: Also it is important to say that the "question mark?" in the...
#...code is too avoid "SQL Injection"

#PART 9.3: (name, ) is a Tuple, as happen with others.

#PART 9.4: The code "IGNORE" means that the program will ignore and...
#...do nothing if I try to "INSERT" a string that already exists. For...
#...instance: if I "INSERT" thee name "Ramses"and that name already...
#exists then the program will "IGNORE" that "INSERT".

#Extra 1: This routine executes an SQL statement...
#...The SQL statement may be parameterized... 
#...(i. e. placeholders instead of SQL literals).... 
#...The sqlite3 module supports two kinds of placeholders: 
#...question marks and named placeholders (named style).

#Extra 2:For example...
#..cursor.execute("insert into people values (?, ?)", (who, age))

#Extra 3: cursor.execute(sql [, optional parameters])

    cur.execute("""INSERT OR IGNORE INTO User (name)
        VALUES ( ? )""", ( name, ) )
    cur.execute("SELECT id FROM User WHERE name = ? ", (name, ))
    
#PART 10.1: This is when we are going to fetch (i.e."Buscar") one record
#...from the "Cursor". Usually there is only one record retrieved...
#...because is is unique.

#PART 10.2: This comment apply also fot he other "cur.fetchone"

#PART 10.3: The zero (0) in the "cur.fetchone" means that there is more...
#than one thing in thata row and I am selecting only the first thing...
#that row.

#PART 10.4: Lo que hice en resumida fue insertar el nombre, luego,...
#..genero el ID dl nombre que inserte y luego pido que dicho ID...
#..que fue generado por el nombre insertado (y que por cierto estan ambos...
#...dentro de la Base de Datos) y pido devuelta ese valor de ID (esto...
#...no quiere decir que lo imprimo), pues los utilizare despues, como...
#se comprueba en la Tabla de MEMBER

#Extra 1: This routine executes an SQL statement...
#...The SQL statement may be parameterized... 
#...(i. e. placeholders instead of SQL literals).... 
#...The sqlite3 module supports two kinds of placeholders: 
#...question marks and named placeholders (named style).

#Extra 2:For example...
#..cursor.execute("insert into people values (?, ?)", (who, age))

#Extra 3: cursor.execute(sql [, optional parameters])

#Extra 4: cursor.fetchone().This method fetches the next row of a...
#...query result set (i.e the result came from a SQLite Database)...,
#...returning a single sequence, or None when no more data is available.

    user_id = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )""", ( title, ) )
    cur.execute("SELECT id FROM Course WHERE title = ? ", (title, ))
    course_id = cur.fetchone()[0]

#PART 11: The code "REPLACE" means that the program will update and...
#...a value if the value that "INSERT" already exists.
    cur.execute("""INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)""",
        ( user_id, course_id, role ) )
    
#PART 12.1: It allow us to extract the info from the disk. It...
#...affect the process and make it slow if it is inside the...
#loop.

#PART 12.2: It write information in the disk; therefore, meanwhile the...
#..."Commit" is executed the program is in pause.

#Extra 1: This method commits (es decir, confirma) the current transaction. 
#If you don't call this method, anything you did since the last call...
#to commit() is not visible from other database connections.

#Extra 2: connection.commit()

conn.commit()

#THE NEXT EXTRAS ARE NO RELATED WITH THE COD BELOW

#Extra 80.1: The JOIN operation link several tables because we cannot find...
#... all th infoin just one table. Therefore, JOIN handle thw work of bring...
#...together those tables to obtaion the info that we need it.

#Extra 80.2: If I use the code of JOIN without the word ON, then the result...
#...Table will show a wrong mix of what we want (i.e. duplicate values).This because the word ON...
#...do establish the link or connection between tables.




