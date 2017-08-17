from functools import reduce
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