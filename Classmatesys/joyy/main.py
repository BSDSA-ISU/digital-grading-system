import sqlite3

from datetime import datetime

DB_NAME = 'library_system.db'

# --- Helper Functions (Reusing setup logic) ---

def get_db_connection():

    return sqlite3.connect(DB_NAME)

def create_database_and_tables():

    # This function is just to ensure tables exist if you run this block separately

    conn = get_db_connection()

    cursor = conn.cursor()

    

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS Book (

        ISBN TEXT PRIMARY KEY,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL,
        Genre TEXT,
        Status TEXT

    )

    ''')

    

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS Patron (

        Patron_ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        College TEXT

    )

    ''')

    

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS LoanTransaction (

        Transaction_ID INTEGER PRIMARY KEY,
        ISBN TEXT,
        Patron_ID INTEGER,
        Borrow_Date DATE NOT NULL,
        Due_Date DATE NOT NULL,
        Return_Date DATE,
        FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
        FOREIGN KEY (Patron_ID) REFERENCES Patron(Patron_ID)

    )

    ''')

    

    conn.commit()

    conn.close()

# --- CRUD Operations ---

def manage_patrons():

    print("\n--- Patron Management ---")

    print("1. Add Patron")

    print("2. View All Patrons")

    print("3. Edit Patron")

    print("4. Delete Patron")

    print("5. Back to Main Menu")

    

    choice = input("Enter choice (1-5): ")

    

    if choice == '1':

        add_patron()

    elif choice == '2':

        view_all('Patron')

    elif choice == '3':

        edit_patron()

    elif choice == '4':

        delete_record('Patron', 'Patron_ID')

    elif choice == '5':

        return

    else:

        print("Invalid choice.")

def add_patron():

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        name = input("Enter Patron Name: ")

        college = input("Enter College/Department: ")

        cursor.execute('INSERT INTO Patron (Name, College) VALUES (?, ?)', (name, college))

        conn.commit()

        print(f"Patron '{name}' added.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()

def edit_patron():

    view_all('Patron')

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        patron_id = int(input("Enter Patron ID to edit: "))

        cursor.execute('SELECT * FROM Patron WHERE Patron_ID = ?', (patron_id,))

        patron = cursor.fetchone()

        

        if patron:

            new_name = input(f"New Name (Current: {patron[1]}): ") or patron[1]

            new_college = input(f"New College (Current: {patron[2]}): ") or patron[2]

            

            cursor.execute('UPDATE Patron SET Name = ?, College = ? WHERE Patron_ID = ?', 

                           (new_name, new_college, patron_id))

            conn.commit()

            print("Patron updated.")

        else:

            print(f"Patron ID {patron_id} not found.")

    except ValueError:

        print("Invalid ID.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()


def manage_books():

    print("\n--- Book Management ---")

    print("1. Add Book")

    print("2. View All Books")

    print("3. Edit Book")

    print("4. Delete Book")

    print("5. Back to Main Menu")

    

    choice = input("Enter choice (1-5): ")

    

    if choice == '1':

        add_book()

    elif choice == '2':

        view_all('Book')

    elif choice == '3':

        edit_book()

    elif choice == '4':

        delete_record('Book', 'ISBN')

    elif choice == '5':

        return

    else:

        print("Invalid choice.")

def add_book():

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        isbn = input("Enter ISBN (Primary Key): ")

        title = input("Enter Title: ")

        author = input("Enter Author: ")

        genre = input("Enter Genre: ")

        status = input("Enter Status (e.g., Available): ")

        cursor.execute('INSERT INTO Book (ISBN, Title, Author, Genre, Status) VALUES (?, ?, ?, ?, ?)', 

                       (isbn, title, author, genre, status))

        conn.commit()

        print(f"Book '{title}' added.")

    except sqlite3.IntegrityError:

        print("Error: ISBN already exists.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()

def edit_book():

    view_all('Book')

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        isbn = input("Enter ISBN to edit: ")

        cursor.execute('SELECT * FROM Book WHERE ISBN = ?', (isbn,))

        book = cursor.fetchone()

        

        if book:

            print(f"Current Title: {book[1]}")

            new_title = input("New Title (Enter to keep): ") or book[1]

            print(f"Current Status: {book[4]}")

            new_status = input("New Status (Enter to keep): ") or book[4]

            

            cursor.execute('UPDATE Book SET Title = ?, Status = ? WHERE ISBN = ?', 

                           (new_title, new_status, isbn))

            conn.commit()

            print("Book updated.")

        else:

            print(f"ISBN {isbn} not found.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()


def manage_transactions():

    print("\n--- Transaction Management (Borrow/Return) ---")

    print("1. Borrow Book (Create Transaction)")

    print("2. Return Book (Update Transaction)")

    print("3. View All Transactions")

    print("4. Back to Main Menu")

    

    choice = input("Enter choice (1-4): ")

    

    if choice == '1':

        borrow_book()

    elif choice == '2':

        return_book()

    elif choice == '3':

        view_all('LoanTransaction')

    elif choice == '4':

        return

    else:

        print("Invalid choice.")

def borrow_book():

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        patron_id = int(input("Enter Patron ID: "))

        isbn = input("Enter ISBN of book borrowed: ")

        

        # Check if Patron and Book exist

        cursor.execute('SELECT Patron_ID FROM Patron WHERE Patron_ID = ?', (patron_id,))

        if not cursor.fetchone():

            print("Error: Patron ID not found.")

            return

            

        cursor.execute('SELECT ISBN, Status FROM Book WHERE ISBN = ?', (isbn,))

        book = cursor.fetchone()

        if not book:

            print("Error: ISBN not found.")

            return

        if book[1] != 'Available':

            print(f"Error: Book {isbn} is currently '{book[1]}'.")

            return

            

        # Set dates (e.g., 14 days loan period)

        borrow_date = datetime.now().strftime('%Y-%m-%d')

        due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

        

        # Insert transaction and update book status

        cursor.execute('INSERT INTO LoanTransaction (Patron_ID, ISBN, Borrow_Date, Due_Date) VALUES (?, ?, ?, ?)', 

                       (patron_id, isbn, borrow_date, due_date))

        cursor.execute('UPDATE Book SET Status = "Loaned" WHERE ISBN = ?', (isbn,))

        

        conn.commit()

        print(f"Transaction created. Due Date: {due_date}")

        

    except ValueError:

        print("Invalid ID format.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()

def return_book():

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        trans_id = int(input("Enter Transaction ID to close: "))

        

        cursor.execute('SELECT ISBN, Return_Date FROM LoanTransaction WHERE Transaction_ID = ?', (trans_id,))

        transaction = cursor.fetchone()

        

        if not transaction:

            print(f"Transaction ID {trans_id} not found.")

            return

        if transaction[1] is not None:

            print(f"Transaction {trans_id} already closed on {transaction[1]}.")

            return

            

        return_date = datetime.now().strftime('%Y-%m-%d')

        

        # Update transaction and book status

        cursor.execute('UPDATE LoanTransaction SET Return_Date = ? WHERE Transaction_ID = ?', (return_date, trans_id))

        cursor.execute('UPDATE Book SET Status = "Available" WHERE ISBN = ?', (transaction[0],))

        

        conn.commit()

        print(f"Book (ISBN: {transaction[0]}) returned successfully on {return_date}.")

        

    except ValueError:

        print("Invalid Transaction ID format.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()


# --- General View/Delete ---

def view_all(table_name):

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(f'SELECT * FROM {table_name}')

        rows = cursor.fetchall()

        

        print(f"\n--- All {table_name} Records ({len(rows)}) ---")

        if not rows:

            print("No records found.")

        else:

            # Simple print for demonstration

            for row in rows:

                print(row)

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()

def delete_record(table_name, pk_column):

    view_all(table_name)

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        pk_value = input(f"Enter the {pk_column} to delete: ")

        

        # Prevent deleting active transactions if possible, but for simplicity, we delete directly

        cursor.execute(f'DELETE FROM {table_name} WHERE {pk_column} = ?', (pk_value,))

        

        if cursor.rowcount > 0:

            conn.commit()

            print(f"{table_name} record with {pk_column}={pk_value} deleted.")

        else:

            print(f"No {table_name} found with {pk_column}={pk_value}.")

    except sqlite3.Error as e:

        print(f"DB Error: {e}")

    finally:

        conn.close()

# --- Data Summary (Option 4 from your screenshot) ---

def view_data_summary():

    print("\n*** Data Summary ***")

    conn = get_db_connection()

    cursor = conn.cursor()

    

    # 1. Descriptive Statistics (Average Loan Duration)

    # Calculate difference in days between Due_Date and Borrow_Date for completed loans

    print("\n--- Descriptive Statistics ---")

    cursor.execute('''

    SELECT AVG(JULIANDAY(Return_Date) - JULIANDAY(Borrow_Date))

    FROM LoanTransaction

    WHERE Return_Date IS NOT NULL;

    ''')

    avg_loan_days = cursor.fetchone()[0]

    if avg_loan_days:

        print(f"Average Loan Duration (Days, completed loans): {avg_loan_days:.2f} days")

    else:

        print("No completed loans found to calculate average duration.")

    # 2. Data Aggregation (Most Frequently Borrowed Genres)

    print("\n--- Data Aggregation ---")

    cursor.execute('''

    SELECT B.Genre, COUNT(T.Transaction_ID) AS TransactionCount

    FROM LoanTransaction T

    JOIN Book B ON T.ISBN = B.ISBN

    GROUP BY B.Genre

    ORDER BY TransactionCount DESC

    LIMIT 5;

    ''')

    top_genres = cursor.fetchall()

    print("Top 5 Most Borrowed Genres:")

    for genre, count in top_genres:

        print(f"- {genre}: {count} transactions")

        

    # Total transactions per patron

    cursor.execute('''

    SELECT P.Name, COUNT(T.Transaction_ID) AS TotalTransactions

    FROM LoanTransaction T

    JOIN Patron P ON T.Patron_ID = P.Patron_ID

    GROUP BY P.Patron_ID

    ORDER BY TotalTransactions DESC

    LIMIT 5;

    ''')

    top_patrons = cursor.fetchall()

    print("\nTop 5 Patrons by Total Transactions:")

    for name, count in top_patrons:

        print(f"- {name}: {count} transactions")

    conn.close()


# --- Main Loop ---

def main_menu():

    # Ensure tables exist before starting the loop

    create_database_and_tables() 

    

    while True:

        print("\n====== Library System Menu ======")

        print("1. Manage Patrons (CRUD)")

        print("2. Manage Books (CRUD)")

        print("3. Manage Transactions (Borrow/Return)")

        print("4. View Data Summary")

        print("5. Exit")

        

        choice = input("Enter your choice (1-5): ")

        

        if choice == '1':

            manage_patrons()

        elif choice == '2':

            manage_books()

        elif choice == '3':

            manage_transactions()

        elif choice == '4':

            view_data_summary()

        elif choice == '5':

            print("Exiting system. Goodbye!")

            break

        else:

            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":

    main_menu()
