from flask import render_template
from . import shl


@shl.app_errorhandler(404)
def page_not_found(e):
    return render_template('info/404.html'), 404


@shl.app_errorhandler(500)
def internal_issues(e):
    return render_template('info/500.html'), 500


@shl.app_errorhandler(405)
def method_not_allowed(e):
    return render_template('info/405.html'), 405