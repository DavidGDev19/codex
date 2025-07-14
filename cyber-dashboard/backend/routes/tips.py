"""Tips blueprint."""

from flask import jsonify

from . import tips_bp


@tips_bp.get("/")
def list_tips():
    """Return tips."""
    return jsonify([])

