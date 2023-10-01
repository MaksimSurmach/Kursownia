import importlib.metadata
import tomllib


def __version__():
    try:
        with open("pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
        __version__ = pyproject["tool"]["poetry"]["version"]
    except Exception as e:
        __version__ = importlib.metadata.version('bop')
    return __version__
