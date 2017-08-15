from pyramid.response import Response
from pyramid.view import view_config
from pyramid.path import AssetResolver
from functools import lru_cache, reduce

def _get_csv_path():
    resolver = AssetResolver()
    csv_asset = resolver.resolve('sampleapp_be:assets/properties.csv')
    csv_path = csv_asset.abspath()
    return csv_path

CSV_PATH = _get_csv_path()

# /
@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {}

# /data
@view_config(route_name='data', renderer='prettyjson', request_method='GET')
def get_data(request):
    # Add this code anywhere you need to enable CORS
    headers = (
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Credentials', 'true'),
        ('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-id, Content-Length, X-Requested-With'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    )
    request.response.headerlist.extend(headers)

    properties = _parse_csv_asset(CSV_PATH)

    return properties

@lru_cache(maxsize=2)
def _parse_csv_asset(path):
    import csv
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        def process_property(property):
            desired_fields = ('PROP_NAME', 'ADDRESS', 'CITY', 'STATE_ID', 'ZIP')
            processed_prop = {field: property[field] for field in desired_fields} 

            # Add MISSING_FIELD_COUNT 
            def get_missing_field_count(prop):
                missing_field_count = reduce(
                    lambda count, field: count if prop[field] else count + 1,
                    prop.keys(),
                    0
                )
                return missing_field_count
            processed_prop['MISSING_FIELD_COUNT'] = get_missing_field_count(property)
            
            # Add MISSING_DATA_ENCODING 
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

            processed_prop['MISSING_DATA_ENCODING'] = get_missing_data_encoding(property)

            return processed_prop
            
        in_cali = lambda prop: prop['STATE_ID'] == 'ca'

        properties = [process_property(property) for property in reader if in_cali(property)]
        return properties

