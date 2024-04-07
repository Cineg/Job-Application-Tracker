import sqlite3
import os
from datetime import date

DB_PATH: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")
TEST_DB_PATH: str = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "test_database.db"
)


##########
# CREATE #
##########
def create_db(db_path: str = DB_PATH) -> bool:
    if os.path.exists(db_path):
        return True

    with open(db_path, "w"):
        pass

    create_offer_table(db_path)
    create_refresh_table(db_path)

    return os.path.exists(db_path)


def create_offer_table(db_path: str = DB_PATH) -> bool:
    if not check_db_exists(db_path, False):
        return False

    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)

        query: str = """
            CREATE TABLE offers (url TEXT PRIMARY KEY UNIQUE, company TEXT, title TEXT, status TEXT, dateAdded TEXT);
        """

        conn.execute(query)
        conn.close()
        return True
    except:
        conn.close()
        return False


def create_refresh_table(db_path: str = DB_PATH) -> bool:
    if not check_db_exists(db_path, False):
        return False
    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)

        query: str = """
            CREATE TABLE refresh (refreshDate TEXT);
        """

        conn.execute(query)
        conn.close()

        if not _add_timestamp(db_path):
            raise Exception

        return True

    except:
        conn.close()
        return False


##########
# UPDATE #
##########
def update_status(
    url: str,
    new_status: str,
    new_title: str,
    new_date: str,
    new_company: str,
    db_path: str = DB_PATH,
) -> bool:
    if not check_db_exists(db_path, False):
        return False

    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()

        if _select_one(url, db_path) is None:
            return False

        query: str = f"""
            UPDATE offers 
            SET 
                status = "{new_status}", 
                title = "{new_title}", 
                dateAdded="{new_date}", 
                company="{new_company}"
            WHERE url = "{url}";
        """

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()

        if not _update_statuses(url, db_path):
            raise Exception

        return True

    except:
        conn.close()
        return False


def _update_statuses(
    url: str = "", db_path: str = DB_PATH, check_timestamp: bool = True
) -> bool:
    if not check_db_exists(db_path, False):
        return False

    try:
        today: str = date.today().strftime("%Y-%m-%d")
        if _get_timestamp(db_path) == today and check_timestamp:
            return True

        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        query: str = f"""
            UPDATE offers 
            SET status = "No response"
            WHERE 
                ROUND(julianday("now") - julianday(dateAdded)) > 30 
                AND
                status = "Applied"
        """

        if url != "":
            if _select_one(url, db_path) is None:
                return False

            query = f"""
            {query} 
            AND 
            url = "{url}";
            """
        else:
            query = f"{query};"

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()

        if not _update_timestamp(db_path):
            raise Exception

        return True

    except:
        conn.close()
        return False


def _update_timestamp(db_path: str = DB_PATH, date: date = date.today()) -> bool:
    if not check_db_exists(db_path, False):
        return False
    try:

        format_date: str = date.strftime("%Y-%m-%d")
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        query: str = f"""
            UPDATE refresh 
            SET refreshDate = "{format_date}"
            WHERE rowid = 1;
        """

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()
        return True

    except:
        conn.close()
        return False


##########
# INSERT #
##########
def add_one_offer(url: str, company: str, title: str, db_path: str = DB_PATH) -> bool:
    try:
        if not check_db_exists(db_path):
            return False

        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        query: str = f"""
            INSERT INTO offers (url, company, title, status, dateAdded)
            VALUES ("{url}", "{company}", "{title}", "Applied", Date("now"));
        """

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


def _add_timestamp(db_path: str = DB_PATH) -> bool:
    if not check_db_exists(db_path):
        return False

    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()

        query: str = """
            INSERT INTO refresh (refreshDate) VALUES (Date("now"))
        """

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


##########
# SELECT #
##########
def select_all(db_path: str = DB_PATH) -> list[list[str]] | None:
    try:
        if not check_db_exists(db_path):
            return None

        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)

        query: str = """
            SELECT 
                rowid as id,
                *
            FROM offers
            ORDER BY dateAdded desc;
        """

        cursor.execute(query)
        result: list[list[str]] = []
        result.append(_get_headers(cursor))

        query_result: list[str] = cursor.fetchall()
        result.append(query_result)

        conn.close()
        return result
    except:
        conn.close()
        return None


def _select_one(url: str, db_path: str = DB_PATH) -> list[list[str]] | None:
    # DEBUG FUNCTION
    try:
        if not check_db_exists(db_path):
            return None

        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)

        query: str = f"""
            SELECT 
                rowid as id,
                *
            FROM offers
            WHERE
            url = '{url}';
        """

        cursor.execute(query)
        result: list[list[str]] = []
        result.append(_get_headers(cursor))

        cursor_res = cursor.fetchone()

        if cursor_res == None:
            raise Exception

        query_result: list[str] = [cursor_res]
        result.append(query_result)

        conn.close()
        return result
    except:
        conn.close()
        return None


def _get_timestamp(db_path: str = DB_PATH) -> str | None:
    if not check_db_exists(db_path, False):
        return None

    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)
        query: str = """
            SELECT * from refresh;
        """

        cursor.execute(query)
        result: str = cursor.fetchone()[0]

        conn.close()
        return result
    except:
        return None


##########
# DELETE #
##########
def delete_offer(url: str, db_path: str = DB_PATH) -> bool:
    if not check_db_exists(db_path, False):
        return False

    if _select_one(url, db_path) is None:
        return False

    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)
        query: str = f"""
            DELETE FROM offers    
            WHERE
            url = "{url}";
        """

        cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


def delete_local_db(db_path: str = DB_PATH) -> bool:
    if not check_db_exists(db_path, False) or ".db" not in db_path:
        return False

    os.remove(db_path)
    return not check_db_exists(db_path, False)


###########
# HELPERS #
###########
def check_db_exists(db_path: str = DB_PATH, attempt_create_db: bool = True) -> bool:
    if os.path.exists(db_path):
        return True

    if attempt_create_db:
        create_db(db_path)

        if os.path.exists(db_path):
            return True

    return False


def _get_headers(cursor: sqlite3.Cursor) -> list[str]:
    headers: list[str] = [item[0] for item in cursor.description]
    return headers


########
# MAIN #
########
def main() -> None:
    pass


if __name__ == "__main__":
    main()
