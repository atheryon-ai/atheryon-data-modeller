import os
from transform.mxml_to_cdm import parse_mxml_to_cdm

def test_parse_mxml_to_cdm():
    # Arrange
    sample_path = "sample_data/sample_trade.mxml"
    assert os.path.exists(sample_path), f"Missing test file: {sample_path}"

    # Act
    result = parse_mxml_to_cdm(sample_path)

    # Assert top-level structure
    assert "Trade" in result
    assert "Party" in result
    assert "Product" in result

    trade = result["Trade"]
    party = result["Party"]
    product = result["Product"]

    # Basic value assertions
    assert trade["status"] == "Active"
    assert party["legal_entity_name"] == "ACME_BANK_LTD"
    assert product["currency"] == "USD"
    assert product["notional"] == 5000000