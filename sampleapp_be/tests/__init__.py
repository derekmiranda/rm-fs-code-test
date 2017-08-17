from unittest import TestCase
from ..models import process_property
import json

def test_process_property():
    with open('tests/sample_property.json') as json_file:
        raw_property = json.load(json_file)
        new_property = process_property(raw_property)
        expected_property = {
            "ADDRESS": "2727 commerical center blvd",
            "CITY": "katy",
            "PROP_NAME": "the grand at lacenterra",
            "STATE_ID": "tx",
            "ZIP": "77494",
            "MISSING_FIELD_COUNT": 0,
            "MISSING_DATA_ENCODING": "24",
        }
        assert new_property == expected_property