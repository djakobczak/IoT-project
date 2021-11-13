from app import app
from settings import settings

import graphs
import callbacks


def main():
    app.config.suppress_callback_exceptions = True
    app.run_server(debug=True, port=settings.PORT, host=settings.HOST)


if __name__ == "__main__":
    main()
