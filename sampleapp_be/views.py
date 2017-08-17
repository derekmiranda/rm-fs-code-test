from pyramid.response import Response
from pyramid.view import view_config
from .helpers import get_csv_path
from .models import get_processed_properties

CSV_PATH = get_csv_path()

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
    properties = get_processed_properties()
    return properties



