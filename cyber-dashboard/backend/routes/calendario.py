"""Calendario blueprint."""

from flask import jsonify

from . import calendario_bp


@calendario_bp.get("/")
def list_calendario():
    """Return calendar events."""
    return jsonify([])

