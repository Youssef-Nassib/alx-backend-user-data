#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, Blueprint
from api.v1.views import app_views

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', methods=['GET'], strict_slashes=False)
def test_unauthorized():
    """Endpoint to test 401 error handler."""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def test_forbidden():
    """Endpoint to test 403 error handler."""
    abort(403)
