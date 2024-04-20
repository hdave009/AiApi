from transformers import pipeline, Pipeline

from constants import DEFAULT_SUMMARY_MIN_LENGTH, DEFAULT_SUMMARY_MAX_LENGTH


class Summarizer:
    model: str = "facebook/bart-large-cnn"
    summarizer: Pipeline = None

    def __init__(self, model: str = "facebook/bart-large-cnn"):
        self.model = model
        self.summarizer = pipeline("summarization", model=model)

    def set_model(self, model: str):
        self.model = model
        self.summarizer = pipeline("summarization", model=model)

    def _sanitize_text(self, text: str):
        # Replace new lines with white spaces.
        text = text.replace('\n', ' ').replace('\r', '')
        return text

    def summarize(self, text: str, min_length=DEFAULT_SUMMARY_MIN_LENGTH, max_length=DEFAULT_SUMMARY_MAX_LENGTH):
        sanitized_text = self._sanitize_text(text)
        return self.summarizer(sanitized_text, max_length=max_length, min_length=min_length, do_sample=True)
