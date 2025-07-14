"""Flask application entry point."""

from flask import Flask, session
from flask_cors import CORS
from .config import DevConfig
from .routes.noticias import noticias_bp
from .routes.tips import tips_bp
from .routes.videos import videos_bp
from .routes.herramientas import herramientas_bp
from .routes.faq import faq_bp
from .routes.calendario import calendario_bp
from .utils.logger import get_logger


app = Flask(__name__)
app.config.from_object(DevConfig)
CORS(app, origins=app.config["ALLOWED_ORIGINS"], supports_credentials=True)
logger = get_logger()


@app.after_request
def set_security_headers(response):
    """Add Content-Security-Policy header."""
    csp = "default-src 'self'"
    response.headers["Content-Security-Policy"] = csp
    return response


@app.before_request
def make_session_permanent():
    """Ensure session uses signed cookies."""
    session.permanent = True


# Register blueprints
app.register_blueprint(noticias_bp)
app.register_blueprint(tips_bp)
app.register_blueprint(videos_bp)
app.register_blueprint(herramientas_bp)
app.register_blueprint(faq_bp)
app.register_blueprint(calendario_bp)


if __name__ == "__main__":
    app.run()
