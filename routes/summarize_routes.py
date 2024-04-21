import requests
from flask import Blueprint, request, jsonify
from ai_models.summarizer import Summarizer
from constants import *

summarize_bp = Blueprint('summarize', __name__)


@summarize_bp.get('/summary_models')
def summary_models():
    models = Summarizer.get_available_summarization_models()
    return sorted(models, reverse=True, key=lambda x: x["likes"])

@summarize_bp.post("/summary")
def summarize_text():
    data = request.get_json()
    summarizer = Summarizer()

    text = data.get("text", None)
    min_len = data.get("min_len", DEFAULT_SUMMARY_MIN_LENGTH)
    max_len = data.get("max_len", DEFAULT_SUMMARY_MAX_LENGTH)
    model = data.get("model", DEFAULT_SUMMARY_MODEL)

    if min_len > max_len:
        return {"errors": ["min_len must be less than max_len."]}, 400


    response = summarizer.summarize(text, min_len, max_len, model)
    summary = response[0].get("summary_text", "")

    return jsonify({"text": summary}), 200
