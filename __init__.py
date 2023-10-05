from . import src as __src__

def create_project(name: str, include_assets: bool = False):
    __src__.builder.create_default_environment(name, include_assets)

__VERSION__ = "0.6.4"