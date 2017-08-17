from functools import lru_cache
from .helpers import process_property, get_csv_path

@lru_cache(maxsize=2)
def parse_csv_asset(path):
    import csv
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        properties = list(reader)
        return properties

def get_processed_properties():
    csv_path = get_csv_path()
    properties = parse_csv_asset(csv_path)
    in_cali = lambda prop: prop['STATE_ID'] == 'ca'
    processed_properties = [process_property(property) for property in properties if in_cali(property)]
    return processed_properties