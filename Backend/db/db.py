import sqlite3
import os

DB_PATH: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")


def check_db_exists() -> bool:
    if os.path.exists(DB_PATH):
        return True

    create_offer_table()
    if os.path.exists(DB_PATH):
        return True

    return False


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


def add_one_offer(url: str, company: str, title: str) -> bool:
    try:
        if not check_db_exists():
            return False

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor: sqlite3.Cursor = conn.cursor()
        query: str = f"""
            INSERT INTO offers (url, company, title, status, dateAdded)
            VALUES ("{url}", "{company}", "{title}", "Applied", DATE("now"));
        """

        cursor = cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


def select_all() -> list[list[str]] | None:
    try:
        if not check_db_exists():
            return None

        conn: sqlite3.Connection = sqlite3.connect(DB_PATH)
        cursor = sqlite3.Cursor(conn)

        query: str = """
            SELECT 
                *,
                ROUND(julianday(dateAdded) - julianday("now")) as dateDiff
            FROM offers;
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
        cursor = sqlite3.Cursor(conn)

        query: str = """
            SELECT 
                *,
                ROUND(julianday(dateAdded) - julianday("now")) as dateDiff
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


def _get_headers(cursor: sqlite3.Cursor) -> list[str]:
    headers: list[str] = [item[0] for item in cursor.description]
    return headers


def main() -> None:
    pass


if __name__ == "__main__":
    main()
