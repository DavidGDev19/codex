"""Herramientas blueprint."""

from flask import jsonify

from . import herramientas_bp


@herramientas_bp.get("/")
def list_herramientas():
    """Return herramientas."""
    return jsonify([])

