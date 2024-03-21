import sqlite3
import os
from datetime import date

DB_PATH: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")


##########
# CREATE #
##########
def create_offer_table() -> bool:
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)

        query: str = """
            CREATE TABLE offers (url TEXT PRIMARY KEY UNIQUE, company TEXT, title TEXT, status TEXT, dateAdded TEXT);
        """

        conn.execute(query)
        conn.close()
        return True
    except:
        conn.close()
        return False


def create_refresh_table() -> bool:
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)

        query: str = """
            CREATE TABLE refresh (refreshDate TEXT);
        """

        conn.execute(query)
        conn.close()

        if not _add_timestamp():
            raise Exception

        return True

    except:
        conn.close()
        return False


##########
# UPDATE #
##########
def update_status(
    url: str, new_status: str, new_title: str, new_date: str, new_company: str
) -> bool:
    try:
        if not check_db_exists():
            return False

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor: sqlite3.Cursor = conn.cursor()
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

        if not _update_statuses(url):
            raise Exception

        return True

    except:
        conn.close()
        return False


def _update_statuses(url: str = "") -> bool:
    try:
        if not check_db_exists():
            return False

        if _get_timestamp() == date.today():
            return True

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
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

        if not _update_timestamp():
            raise Exception

        return True

    except:
        conn.close()
        return False


def _update_timestamp() -> bool:
    try:
        if not check_db_exists():
            return False

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor: sqlite3.Cursor = conn.cursor()
        query: str = f"""
            UPDATE refresh 
            SET refreshDate = date("now")
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
def add_one_offer(url: str, company: str, title: str) -> bool:
    try:
        if not check_db_exists():
            return False

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
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


def _add_timestamp() -> bool:
    try:
        if not check_db_exists():
            return False
        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
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
def select_all() -> list[list[str]] | None:
    try:
        if not check_db_exists():
            return None

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
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


def _select_one() -> list[list[str]] | None:
    # DEBUG FUNCTION
    try:
        if not check_db_exists():
            return None
        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)

        query: str = """
            SELECT 
                rowid as id,
                *
            FROM offers
            WHERE
            url = "https://github.com/Cineg";
        """

        cursor.execute(query)
        result: list[list[str]] = []
        result.append(_get_headers(cursor))

        query_result: list[str] = [cursor.fetchone()]
        result.append(query_result)

        conn.close()
        return result
    except:
        conn.close()
        return None


def _get_timestamp() -> str | None:
    try:
        if not check_db_exists():
            return None

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor: sqlite3.Cursor = sqlite3.Cursor(conn)
        query: str = """
            SELECT * from refresh;
        """

        cursor.execute(query)
        result: str = cursor.fetchone()

        conn.close()
        return result
    except:
        return None


##########
# DELETE #
##########
def delete_offer(url: str) -> bool:
    try:
        if not check_db_exists():
            return False

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
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


###########
# HELPERS #
###########
def check_db_exists() -> bool:
    if os.path.exists(DB_PATH):
        return True

    create_offer_table()
    create_refresh_table()

    if os.path.exists(DB_PATH):
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
