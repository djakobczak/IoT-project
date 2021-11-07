from app import app

from graphs import update_graph


def main():
    app.run_server(debug=True, port=9000, host="0.0.0.0")  # !TODO use env file/external config


if __name__ == "__main__":
    main()
