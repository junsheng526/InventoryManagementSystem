import sqlite3

def add_due_date_column():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE tasks ADD COLUMN due_date TEXT")
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# add_due_date_column()

def delete_first_four_rows():
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        # Select the first 4 rows
        cursor.execute("SELECT id FROM tasks ORDER BY id LIMIT 4")
        rows = cursor.fetchall()
        
        if rows:
            # Create a list of ids to delete
            ids_to_delete = [row[0] for row in rows]
            
            # Use the list of ids to delete the rows
            cursor.execute("DELETE FROM tasks WHERE id IN ({})".format(",".join("?" * len(ids_to_delete))), ids_to_delete)
            
            # Commit the changes
            conn.commit()
            print(f"Deleted rows with ids: {ids_to_delete}")
        else:
            print("No rows to delete.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()

# Run the function to delete the first 4 rows
delete_first_four_rows()