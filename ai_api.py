from flask import Flask
from flask_cors import CORS
from routes.summarize_routes import summarize_bp
from dotenv import load_dotenv

API_ROUTE_PREFIX = "api"

def create_app():
    flask_app = Flask(__name__)
    cors = CORS(flask_app)

    flask_app.register_blueprint(summarize_bp, url_prefix=f"/{API_ROUTE_PREFIX}")

    return flask_app

app = create_app()
if __name__ == "__main__":
    load_dotenv()
    app.run(host="0.0.0.0", port=8080, debug=True)
