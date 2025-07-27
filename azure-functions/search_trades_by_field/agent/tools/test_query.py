from pprint import pprint

from query_tool import search_trades_by_field

if __name__ == "__main__":
    result = search_trades_by_field("legal_entity_name", "ACME_BANK_LTD")
    pprint(result)
