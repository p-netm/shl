from flask import render_template
from . import shl


@shl.app_errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@shl.app_errorhandler(500)
def internal_issues():
    return render_template('500.html'), 500