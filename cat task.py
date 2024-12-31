users = {}
def add_user(username, email):
    if username in users:
        print(f"User '{username}' already exists.")
    else:
        users[username] = email
        print(f"User '{username}' added.")
def view_user(username):
    if username in users:
        print(f"Username: {username}, Email: {users[username]}")
    else:
        print(f"User '{username}' not found.")
def delete_user(username):
    if username in users:
        del users[username]
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' not found.")
def list_users():
    if users:
        for username, email in users.items():
            print(f"Username: {username}, Email: {email}")
    else:
        print("No users found.")