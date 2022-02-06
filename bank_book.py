from tkinter import *
from tkinter import messagebox, Tk
import sqlite3
from tkinter import Entry

# creating the size of the window
root: Tk = Tk()
root.geometry("500x800")

# connecting to a database to enable sort, edit and delete functions. Naming it Bank_book
# this is an initial connection to make sure there is a table for the program to work in.
initial_connection = sqlite3.connect("Bank_book.db")
# create a cursor
initial_cursor = initial_connection.cursor()
# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                name text,
                accountnumber text,
                date text,
                shop text,
                amount text,
                category text

                )""")

# commit changes to database
initial_connection.commit()
# close the initial cursor
initial_cursor.close()
# then close the initial connection to the database
initial_connection.close()


# there are no tables named "tableName"

# Creating add function
def add():
    # Ask if user is sure to add data entered
    answer = messagebox.askyesno('prompt', 'Do you want to add the transaction data? ')

    # if the user says yes, execute the main part of the function
    if answer:
        # open a connection to the database
        connection = sqlite3.connect("Bank_book.db")
        # create a cursor
        cur = connection.cursor()
        # Insert entries into table if statement true and clear entry boxes
        cur.execute("INSERT INTO transactions VALUES (:e_name, :e_account, :e_date, :e_shop, :e_amount, :e_category)",
                    {
                        'e_name': e_name.get(),
                        'e_account': e_account.get(),
                        'e_date': e_date.get(),
                        'e_shop': e_shop.get(),
                        'e_amount': e_amount.get(),
                        'e_category': e_category.get(),
                    })

        # delete text in the entry boxes after the insert operation
        e_name.delete(0, END)
        e_account.delete(0, END)
        e_date.delete(0, END)
        e_shop.delete(0, END)
        e_amount.delete(0, END)
        e_category.delete(0, END)


        messagebox.showinfo("Success!", "Successfully added a transaction!")

        # commit changes to database
        connection.commit()
        # close the cursor
        cur.close()
        # Close connection to database when function is not running
        connection.close()

    # if user selects no, then do nothing
    elif not answer:
        pass

    # if there is an error, print it
    else:
        messagebox.showerror('Error', 'something went wrong!')


# Create function so the user can check what he/she has inputted
def query():
    # Ask if user wants to check/fetch all data
    answer = messagebox.askyesno('prompt', 'Do you want to check your data? ')
    # if the user says yes, execute the main part of the function
    if answer == True:

        # open a connection to the database
        connection = sqlite3.connect("Bank_book.db")
        # create a cursor
        cur = connection.cursor()

        # query the database, and see what information have been added by execute sequel command and primary key
        cur.execute("SELECT oid,* FROM transactions")
        elements = cur.fetchall()
        # print(elements)

        print_elements = ''
        if not elements:
            # if there are no records in the database
            print_elements = 'No records found'
            messagebox.showinfo("Info", "No records found")

        else:
            # Loop through results and present a new transaction on a new line
            for element in elements:
                print_elements += str(element) + "\n"

        # Data fetched by this method to be displayed on the screen // output data
        # Clear the label before displaying data
        query_label.config(text='')
        query_label.config(text=print_elements)

        # commit changes to database, necessary for each function
        connection.commit()
        # close the cursor
        cur.close()
        # Close connection to database when function is not running
        connection.close()

    # if user selects no, then do nothing
    elif not answer:
        pass

    # if there is an error, print it
    else:
        messagebox.showerror('Error', 'something went wrong!')


# create function to sort transactions by amount
def sort_by_amount():
    # Ask if user is sure to sort by amount
    answer = messagebox.askyesno('Prompt', 'Do you want to sort your data by amount? ')
    # if the user says yes, execute the main part of the function
    if answer == True:

        # open a connection to the database
        connection = sqlite3.connect("Bank_book.db")
        # create a cursor
        cur = connection.cursor()

        # define sort entry and execute to fetch data from database
        cur.execute("SELECT oid, * FROM transactions ORDER BY amount ASC")
        elements = cur.fetchall()
        # print(elements)

        print_elements = ''
        if not elements:
            # if there are no records in the database let the user know
            print_elements = 'No records found'
            messagebox.showinfo("Info", "No records found")

        else:
            # Loop through results and present a new row on a new line
            for element in elements:
                print_elements += str(element) + "\n"

        # Data fetched by this method to be displayed on the screen // output data
        # Clear the label before displaying data
        query_label.config(text='')
        query_label.config(text=print_elements)

        # commit changes to database, necessary for each function
        connection.commit()
        # close the cursor
        cur.close()
        # close connection to database when function is not running
        connection.close()

    # if user selects no, then do nothing
    elif not answer:
        pass
    # if there is an error, print it
    else:
        messagebox.showerror('Error', 'no data to be displayed!')


# Creating function to only delete one specific record. Must connect to the database and create cursor for this function
def delete():
    answer = messagebox.askyesno('prompt', 'Do you want to delete? ')
    # if the user says yes, execute the main part of the function
    if answer == True:

        # open a connection to the database
        connection = sqlite3.connect("Bank_book.db")
        # create a cursor
        cur = connection.cursor()

        # defining SQL statement, which row to delete
        cur.execute("DELETE from transactions WHERE oid=?", (delete_text.get(),))

        delete_text.delete(0, END)

        # commit changes to database, necessary for each function
        connection.commit()
        # close the cursor
        cur.close()
        # Close connection to database when function is not running
        connection.close()

    # if user selects no, then do nothing
    elif not answer:
        pass
    # if something went wrong
    else:
        messagebox.showerror('error', 'something went wrong!')


def search():
    # search by this word. Will only find something if it is a date though
    search_term = e_search_date.get()

    answer = messagebox.askyesno('prompt', 'Do you want to search for date: {}? '.format(search_term))
    # if the user says yes, execute the main part of the function
    if answer == True:

        # open a connection to the database
        connection = sqlite3.connect("Bank_book.db")
        # create a cursor
        cur = connection.cursor()

        # define search entry by date and execute to fetch data from database
        cur.execute("SELECT oid, * FROM transactions WHERE date=?", (search_term,))
        dates_found = cur.fetchall()
        # print(dates_found)

        date_found = ''
        # if no dates found
        if not dates_found:
            date_found = "No records with {} found".format(search_term)
            messagebox.showinfo("information", "No date match. Try again.")

        # if dates found
        else:
            # Loop through results and present results on new line
            for element in dates_found:
                date_found += str(element) + "\n"

        # Data fetched by this method to be displayed on the screen // output data
        # Clear the label before displaying data
        query_label.config(text='')
        query_label.config(text=date_found)

        # commit changes to database, necessary for each function
        connection.commit()
        # close the cursor
        cur.close()
        # close connection to database when function is not running
        connection.close()

    # if user selects no, then do nothing
    elif not answer:
        pass
    # if something went wrong
    else:
        messagebox.showerror('error', 'something went wrong!')


# creating delete label for my delete entry box and placement on the screen
delete_text_label = Label(root, text="Enter the number of the row you wish to delete")
delete_text_label.grid(row=19, column=1, pady=5, padx=5)

# creating label to specify where data is displayed placing it on the screen
query_label = Label(root, text="data will be displayed here")
query_label.grid(row=37, column=0, columnspan=9)

# creating search label for my search entry box and placing on the screen
search_date_Label = Label(root, text="Enter the date of wish to search for")
search_date_Label.grid(row=30, column=1, pady=5, padx=5)

# Create add button so records can be added to my table in sql
add_ = Button(root, text="Add transaction data", command=add)
add_.grid(row=15, columnspan=3, ipadx=90, pady=5, padx=5)

# Create button to see information entered
check_button = Button(root, text="Check records", command=query)
check_button.grid(row=16, column=0, columnspan=3, ipadx=110, pady=5, padx=5)

# Create search button
search_date_Button = Button(root, text="Search transactions", command=search)
search_date_Button.grid(row=33, column=0, columnspan=3, ipadx=100, pady=10, padx=10)

# Create button to delete a specific entry
delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=21, column=0, columnspan=3, ipadx=140, pady=10, padx=10)

# Creating drop down menu to allow user to choose how to sort results list
sort_dec_button = Button(root, text="Sort transactions in descending order by amount", command=sort_by_amount)
sort_dec_button.grid(row=35, column=0, columnspan=3, ipadx=15, pady=10, padx=10)

# creating entry box to search for item, text in box and placing on the screen
e_search_date = Entry(root, width=35)
e_search_date.grid(row=31, column=1, pady=5, padx=5)
e_search_date.insert(0, "Enter date you wish to search for")

# creating entry box for transaction to be deleted, adding text in the box and placing on the screen
delete_text = Entry(root, width=35, borderwidth=1)
delete_text.grid(row=20, column=1)
delete_text.insert(8, "Enter the row number you want deleted")

# Creating entries for the user to input name, account number, date, shop name, amount and category
e_name = Entry(root, width=35, borderwidth=1)
e_name.grid(row=0, column=1, padx=5, pady=(30, 0))
e_name.get()
e_name.insert(0, "Enter your name")

# Creating entry box for account number and adding text in the boxes so the user know what to type,
# and placing it on the screen
e_account = Entry(root, width=35, borderwidth=1)
e_account.grid(row=1, column=1, padx=5)
e_account.get()
e_account.insert(1, "Enter your account number: ")

# Creating entry box for account number and adding functions
e_date = Entry(root, width=35, borderwidth=1)
e_date.grid(row=2, column=1, padx=5)
e_date.get()
e_date.insert(2, "Enter the date of the transaction: ")

# Creating entry for the user to input amount of transaction
e_shop = Entry(root, width=35, borderwidth=1)
e_shop.grid(row=3, column=1, padx=5)
e_shop.get()
e_shop.insert(4, "Enter the shop name:")

# Creating entry for the user to input amount of transaction
e_amount = Entry(root, width=35, borderwidth=1)
e_amount.grid(row=4, column=1, padx=5)
e_amount.insert(3, "Enter the amount of the transaction")
#print(e_amount.get())

# Creating entry for the user to input amount of transaction
e_category = Entry(root, width=35, borderwidth=1)
e_category.grid(row=5, column=1, padx=5)
e_category.get()
e_category.insert(5, "Enter category")

root.mainloop()