from flask import render_template, redirect, Blueprint
from domcek.api import service

blueprint = Blueprint('registration', __name__)


# This is endpoint which should download whole database users registered to event
@blueprint.route("/list", methods=['GET'])
def download():
    service.download()
    return 'hlist'


# This is endpoint responsible for uploading changes to server after registration end
@blueprint.route("/upload", methods=['POST'])
def upload():
    service.upload()
    return redirect('/')
