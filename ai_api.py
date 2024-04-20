from flask import Flask
from routes.summarize_routes import summarize_bp

API_ROUTE_PREFIX = "api"

def create_app():
    flask_app = Flask(__name__)

    flask_app.register_blueprint(summarize_bp, url_prefix=f"/{API_ROUTE_PREFIX}")

    return flask_app

app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
