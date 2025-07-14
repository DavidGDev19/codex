"""Package for API routes."""

from flask import Blueprint

noticias_bp = Blueprint("noticias", __name__, url_prefix="/api/noticias")
tips_bp = Blueprint("tips", __name__, url_prefix="/api/tips")
videos_bp = Blueprint("videos", __name__, url_prefix="/api/videos")
herramientas_bp = Blueprint("herramientas", __name__, url_prefix="/api/herramientas")
faq_bp = Blueprint("faq", __name__, url_prefix="/api/faq")
calendario_bp = Blueprint("calendario", __name__, url_prefix="/api/calendario")
