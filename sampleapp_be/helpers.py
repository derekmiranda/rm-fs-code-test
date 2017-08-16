from functools import lru_cache, reduce
from pyramid.path import AssetResolver

def get_csv_path():
    resolver = AssetResolver()
    csv_asset = resolver.resolve('sampleapp_be:assets/properties.csv')
    csv_path = csv_asset.abspath()
    return csv_path

def get_missing_field_count(prop):
    missing_field_count = reduce(
        lambda count, field: count if prop[field] else count + 1,
        prop.keys(),
        0
    )
    return missing_field_count

def get_missing_data_encoding(prop):
    encoded_num_builder = ""
    curr_num = 0
    on_columns_with_data = None

    for field in prop.keys():
        val = prop[field]
        field_has_data = bool(val)

        if on_columns_with_data is None:
            curr_num = 1
        else:
            # if in same data state, add 1 to curr_num
            if on_columns_with_data == field_has_data:
                curr_num += 1
            else:
                # append curr_num to num_builder
                encoded_num_builder += str(curr_num)
                # reset curr_num to 1
                curr_num = 1
        on_columns_with_data = field_has_data

    encoded_num_builder += str(curr_num)
    return int(encoded_num_builder)

def process_property(property):
    desired_fields = ('PROP_NAME', 'ADDRESS', 'CITY', 'STATE_ID', 'ZIP')
    processed_prop = {field: property[field] for field in desired_fields} 
    processed_prop['MISSING_FIELD_COUNT'] = get_missing_field_count(property)
    processed_prop['MISSING_DATA_ENCODING'] = get_missing_data_encoding(property)
    return processed_prop

@lru_cache(maxsize=2)
def parse_csv_asset(path):
    import csv
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        in_cali = lambda prop: prop['STATE_ID'] == 'ca'
        properties = [process_property(property) for property in reader if in_cali(property)]
        return properties