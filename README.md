# Bank book

This folder contains the first coding assignment of MSc Computer Science November 2021 from the Launching into Computer Science from the 
University of Essex Online.
@ Author, Maja Tagt




## Table of contents
    Aim
    Structure of the code
    Technologies used
    Dependencies
    Scope
    	widgets
	sql statements
    Data storage
    Test strategy
    Test results
    Project status	
    Concluding remarks
   
## Aim of the bank book 
The set-out purpose of the bank book is to allow the user to enter and store data about their transactions. Created with Python, SQLite 3 and Tkinter. 


## Structure of the code
1. Imports of libraries
2. Database table created in SQL; only runs once
3. Functions add, query, sort_by_amount, delete and search. 
4. Structure of each function, see the explanation of SQL statements under the SQL statements section. 

```
Def function():
answer = messagebox.askyesno
if answer == True:
	function executes
if not variable found
	messagebox.showinfo(“error message”)
else:
loop through result and present results on new line 
```

4.	Labels created
5.	Buttons created
6.	Entry boxes created


## Technologies used
Python 3.10
SQLite 3
Tkinter
  message box
  entry

### Dependencies
Latast drivers 
the libraries need to be imported and it must be run in an environment. Imports should already be in the code.

```
from tkinter import *
from tkinter import messagebox, Tk
import sqlite3
from tkinter import Entry
```

## Scope of functionalities and break down of the code
user can enter six records
user can delete, and search records based on keywords
user can sort the records by amount
user gets a prompt on the screen before committing to an action
user must select an option on the screen for a function to be performed

Entry boxes are used to permit the user to input its own data. In the code I have used six and they follow a similar pattern like this:

```
entrybox_name = Entry(root, width=X, borderwidth=X)
entrybox_name.grid(row=X, column=X, padx=X, pady=(X, X))
entrybox_name.get()
entrybox.insert(0, "Text visible in entry box")
```

the top row dictates to the program it is an entry box, placed in the root folder with its dimensions specified. The second row specifies the placement of the entry box, where the third row is a get method used in the add function, so the program knows where to insert what data in the SQL database. 

### widgets
With widgets created in Tkinter using buttons and labels, data is fetched using Python functions from the SQL database table and presented on the screen for the user. For example, to create the “check records” button the command statement fetches instructions from the specified function. In this example, the query function is called to execute, to add records the add function is fetched etc. The second line dictates where the button is placed on the screen in relation to the other buttons.

```
Button_variable = Button(root, text="Text visible in box", command=query)
check_button.grid(row=X, column=X, columnspan=X, ipadx=X, pady=X, padx=X)
```

Labels are used to inform the user what information is required or where data is displayed. In some instances I have opted for the instructions to be in the entry boxes, but I have also created labels that hopefully helps the user understand the program. For example, my query_label lets the user know where it can expect the entered data to be outputted. 

```
query_label = Label(root, text="data will be displayed here")
query_label.grid(row=37, column=0, columnspan=9)
equates to this on the GUI:
```

### SQL statements
The code throughout follows the main structure but changed to suit each function. Each variable is named after what it is supposed to do to ensure its intended use is clear. Additionally, SQL statements are included in each function as a connection to the database is established and closed after executing a function, instead of implementing a global scoped connection that all functions access at run time. Therefore, each function follows the following blueprint: 

1.	Create connection
2.	Create cursor
3.	Create Query string
4.	Execute the query
5.	Commit to the query
6.	Close the cursor
7.	Close the connection

## Data storage
The data fetched comes in tuples, so some formatting is required before the program displays the results to the user. In this case I want to display the results in an entry box, and the simplest way is to convert the tuples to strings, and then add a line break at the end of each row with backslash plus n, \n, to get a separate line for each result.


## Test strategy 
Run the code and Tkinter GUI should appear. Enter test data as specified in part 1 and click “add transaction data”. Follow the test strategy table as below.
https://github.com/majatagt/assignment-part-2/blob/a0b4fea41da10fe1531b28d5f79c13ed346591b3/Screenshot%202022-02-03%20at%2012.23.09.png

 
  

## Test strategy results
 https://github.com/majatagt/assignment-part-2/blob/a0b4fea41da10fe1531b28d5f79c13ed346591b3/Screenshot%202022-02-02%20at%2017.15.11.png


My testing strategy in film. 





## Project status 
Finalised.

## Concluding remarks, notes, and scope for improvement
Functions I would have done differently:

Instead of sorting the records by amount in descending order, I would have enabled sorting by date or category instead.
