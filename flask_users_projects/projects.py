#!/usr/bin/env python3
import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_users_projects.db import get_db

bp = Blueprint("projects", __name__, url_prefix="/proyecto")
