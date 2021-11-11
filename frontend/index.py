from app import app

import graphs
import callbacks


def main():
    app.config.suppress_callback_exceptions = True
    app.run_server(debug=True, port=9000, host="0.0.0.0")  # !TODO use env file/external config


if __name__ == "__main__":
    main()
