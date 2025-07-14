"""FAQ blueprint."""

from flask import jsonify

from . import faq_bp


@faq_bp.get("/")
def list_faq():
    """Return FAQ."""
    return jsonify([])

