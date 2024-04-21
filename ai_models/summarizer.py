from transformers import pipeline, Pipeline
from constants import *
import requests
import os

class Summarizer:
    model: str = "facebook/bart-large-cnn"

    def __init__(self, model: str = "facebook/bart-large-cnn"):
        self.model = model

    def set_model(self, model: str):
        self.model = model

    def _sanitize_text(self, text: str):
        # Replace new lines with white spaces.
        text = text.replace('\n', ' ').replace('\r', '')
        return text

    def summarize(self, text: str, min_length=DEFAULT_SUMMARY_MIN_LENGTH, max_length=DEFAULT_SUMMARY_MAX_LENGTH, model=None):

        if model:
            self.set_model(model)

        sanitized_text = self._sanitize_text(text)

        endpoint = f"{INFERENCE_API_DOMAIN}{self.model}"
        token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

        headers = {"Authorization": f"Bearer {token}"}

        payload = {
            "inputs": sanitized_text,
            "parameters": {
                "do_sample": True,
                "min_length": min_length,
                "max_length": max_length,
            },
            "options": {
                "use_cache": True,
                "wait_for_model": True
            }
        }

        response = requests.post(endpoint, headers=headers, json=payload)

        return response.json()

    @staticmethod
    def get_available_summarization_models():
        endpoint = f"{HUGGINGFACE_API_DOMAIN}models?pipeline_tag=summarization"
        response = requests.get(endpoint)
        return [{ "id": model.get("id"), "modelId": model.get("modelId"), "likes": model.get("likes"), "downloads": model.get("downloads") } for model in response.json()]
