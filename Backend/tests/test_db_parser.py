from ..db.db import TEST_DB_PATH, _select_one, add_one_offer
from ..src.db_parser import parse_db_query


def test_parse_db_query() -> None:
    add_one_offer("a", "a", "a", TEST_DB_PATH)
    query: list[list[str]] | None = _select_one("a", TEST_DB_PATH)
    if query is not None:
        res = parse_db_query(query)

        assert "Offers" in res
        assert res["Offers"][0]["url"] != None
        assert res["Offers"][0]["company"] != None
        assert res["Offers"][0]["title"] != None
