import json
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime


def parse_mxml_to_cdm(mxml_path: str) -> dict:
    tree = ET.parse(mxml_path)
    root = tree.getroot()

    # Namespaces (if any)
    ns = {'mx': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    def find(xpath):
        return root.find(xpath, ns)

    def get_text_or_raise(xpath):
        el = find(xpath)
        if el is None or el.text is None:
            raise ValueError(f"Missing required element or text for xpath: {xpath}")
        return el.text

    trade_id = str(uuid.uuid4())
    product_id = str(uuid.uuid4())
    party_id = str(uuid.uuid4())

    # Extract values
    trade_date = get_text_or_raise('.//mx:tradeHeader/mx:tradeDate')
    legal_entity_name = get_text_or_raise('.//mx:party[1]/mx:partyId')
    currency = get_text_or_raise('.//mx:product/mx:currency')
    notional = float(get_text_or_raise('.//mx:product/mx:notionalAmount'))
    maturity_date = get_text_or_raise('.//mx:product/mx:maturityDate')

    # Build CDM-compatible object
    return {
        "Party": {
            "party_id": party_id,
            "legal_entity_name": legal_entity_name,
            "identifier": legal_entity_name,
            "role": "Counterparty",
        },
        "Product": {
            "product_id": product_id,
            "product_type": "InterestRateSwap",  # default for now
            "asset_class": "Rates",
            "currency": currency,
            "notional": notional,
            "maturity_date": maturity_date,
        },
        "Trade": {
            "trade_id": trade_id,
            "trade_reference": f"{legal_entity_name}-{trade_date}",
            "trade_date": trade_date,
            "booking_location": "Default",
            "counterparty_id": party_id,
            "product_id": product_id,
            "status": "Active",
            "execution_venue": "N/A",
            "comments": None,
        },
    }


if __name__ == "__main__":
    from pprint import pprint

    try:
        result = parse_mxml_to_cdm("sample_data/sample_trade.mxml")
        pprint(result)

        with open("output/trade_cdm.json", "w") as f:
            json.dump(result, f, indent=2)
        print("📝 Output written to output/trade_cdm.json")
        print("\n✅ Transformation complete.")
    except Exception as e:
        print(f"\n❌ Failed to parse MxML: {e}")
