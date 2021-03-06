import os
import sys

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')
app.config.from_object('config')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

import pmp.views
