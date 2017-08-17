from functools import lru_cache
from .helpers import get_csv_path

@lru_cache(maxsize=2)
def parse_csv_asset(path):
    import csv
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        properties = list(reader)
        return properties

def process_property(property):
    desired_fields = ('PROP_NAME', 'ADDRESS', 'CITY', 'STATE_ID', 'ZIP')
    processed_prop = {field: property[field] for field in desired_fields} 
    processed_prop['MISSING_FIELD_COUNT'] = get_missing_field_count(property)
    processed_prop['MISSING_DATA_ENCODING'] = get_missing_data_encoding(property, '-')
    return processed_prop

@lru_cache(maxsize=2)
def get_processed_properties():
    csv_path = get_csv_path()
    properties = parse_csv_asset(csv_path)
    in_cali = lambda prop: prop['STATE_ID'] == 'ca'
    processed_properties = [process_property(property) for property in properties if in_cali(property)]
    return processed_properties