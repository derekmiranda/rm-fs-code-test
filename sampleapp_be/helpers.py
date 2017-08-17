from functools import reduce
from pyramid.path import AssetResolver

def get_csv_path():
    resolver = AssetResolver()
    csv_asset = resolver.resolve('sampleapp_be:assets/properties.csv')
    csv_path = csv_asset.abspath()
    return csv_path