def parse_db_query(query_result: list[list[str]]) -> dict[str, list[dict]]:
    results: dict[str, list[dict]] = {"Offers": []}
    for query_item in query_result[1]:
        item: dict = {}
        for index, value in enumerate(query_item):

            item[query_result[0][index]] = value

        results["Offers"].append(item)

    return results


def main() -> None:
    pass


if __name__ == "__main__":
    main()
