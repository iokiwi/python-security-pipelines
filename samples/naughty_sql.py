def check_login(username: str, password: str, db_connection) -> bool:

    cursor = db_connection.cursor()
    query = (
        "SELECT * FROM users WHERE"
        f"username = '{username}' AND password = '{password}'"
  	)

    result = cursor.execute(query).fetchone()

    if result:
        return True
    return False
