import glob
import json


def search_trades_by_field(field: str, value: str):
    """Searches all trades for a match on a top-level Trade or Party field"""
    matches = []
    for path in glob.glob("canonical_store/trades/*.json"):
        with open(path) as f:
            obj = json.load(f)
            trade = obj.get("Trade", {})
            party = obj.get("Party", {})

            if field in trade and str(trade[field]) == value:
                matches.append(obj)
            elif field in party and str(party[field]) == value:
                matches.append(obj)

    return matches
