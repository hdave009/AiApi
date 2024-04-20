import requests
from flask import Blueprint, request, jsonify

from ai_models.summarizer import Summarizer
from constants import DEFAULT_SUMMARY_MIN_LENGTH, DEFAULT_SUMMARY_MAX_LENGTH

summarize_bp = Blueprint('summarize', __name__)


@summarize_bp.get("/summary")
def summarize_text():
    data = request.get_json()
    summarizer = Summarizer()

    text = data.get("text", None)
    min_len = data.get("min_len", DEFAULT_SUMMARY_MIN_LENGTH)
    max_len = data.get("max_len", DEFAULT_SUMMARY_MAX_LENGTH)

    if min_len > max_len:
        return {"errors": ["min_len must be less than max_len."]}, 400

    summary = summarizer.summarize(text, min_len, max_len)[0].get("summary_text", "")

    return jsonify({"text": summary}), 200
