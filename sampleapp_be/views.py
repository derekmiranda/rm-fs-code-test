from pyramid.response import Response
from pyramid.view import view_config


# /
@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {}

# /data
@view_config(route_name='data', renderer='json', request_method='GET')
def get_data(request):
    # Add this code anywhere you need to enable CORS
    headers = (
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Credentials', 'true'),
        ('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-id, Content-Length, X-Requested-With'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    )
    request.response.headerlist.extend(headers)

    csv_path = request.static_path('sampleapp_be:assets/properties.csv')
    _parse_csv_asset(csv_path)

    return {}

def _parse_csv_asset(path):
    print(path)
    # check cached dict
    # if none, then parse csv

    # import csv
    # with open(
