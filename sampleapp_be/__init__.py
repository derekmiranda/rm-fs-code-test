from pyramid.config import Configurator
from pyramid.renderers import JSON


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_renderer('prettyjson', JSON(indent=4))
    config.add_route('home', '/')
    config.add_route('data', '/data')
    config.add_static_view(name='assets', path='sampleapp_be:assets')
    config.scan('.views')
    return config.make_wsgi_app()
