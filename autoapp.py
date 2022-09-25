from flask.helpers import get_debug_flag

from src.api.app import create_app
from src.api.settings import DevConfig, ProdConfig


if __name__ == '__main__':
    CONFIG = DevConfig
    app = create_app(CONFIG)
    app.run(debug=True)
