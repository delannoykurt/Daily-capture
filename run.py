from app import create_app


PORT = 5099
app = create_app()

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
