from functools import lru_cache
from .helpers import get_csv_path

@lru_cache(maxsize=2)
def parse_csv_asset(path):
    import csv
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        properties = list(reader)
        return properties


def get_missing_field_count(prop):
    missing_field_count = reduce(
        lambda count, field: count if prop[field] else count + 1,
        prop.keys(),
        0
    )
    return missing_field_count

def get_missing_data_encoding(prop, separator):
    encoded_num_builder = []
    curr_num = 0
    on_columns_with_data = None
    add_num = lambda num: encoded_num_builder.append(str(num))    

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
                add_num(curr_num)
                # reset curr_num to 1
                curr_num = 1
        on_columns_with_data = field_has_data
    add_num(curr_num)
    return separator.join(encoded_num_builder)

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