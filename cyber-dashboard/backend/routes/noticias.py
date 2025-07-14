"""Noticias blueprint."""

from flask import jsonify, request

from . import noticias_bp
from ..utils.security import sanitize_str


@noticias_bp.get("/")
def list_noticias():
    """Return sanitized noticias."""
    query = sanitize_str(request.args.get("q", ""))
    return jsonify({"results": [], "query": query})

