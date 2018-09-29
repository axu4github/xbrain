# coding=utf-8

from xbrain.similarity import Word2VectorSimilarity
from xbrain.apis.responses import SuccessResponse, FailedResponse
from flask import Blueprint, request


apis = Blueprint("apis", __name__, url_prefix="/apis")


@apis.route("/similar", methods=("POST", ))
def similar():
    try:
        corpus = request.form["corpus"]
        words = request.form["words"].split(",")
        is_segment = bool(request.form["is_segment"])
        similars = Word2VectorSimilarity(
            corpus, is_segment=is_segment, min_count=1).most_similar(words)
        response = SuccessResponse(similars)
    except Exception as e:
        response = FailedResponse(str(e))

    return str(response)
