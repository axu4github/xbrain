# coding=utf-8

from flask import Blueprint
from xbrain.similarity import Similarity

apis = Blueprint("apis", __name__, url_prefix="/apis")


@apis.route("/similar", methods=("POST", ))
def similar():
    return Similarity().most_similar()
