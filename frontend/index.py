from app import app

from graphs import update_graph


def main():
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
