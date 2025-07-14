"""Videos blueprint."""

from flask import jsonify

from . import videos_bp


@videos_bp.get("/")
def list_videos():
    """Return videos."""
    return jsonify([])

