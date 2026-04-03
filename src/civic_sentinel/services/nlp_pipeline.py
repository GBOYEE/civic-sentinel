"""NLP pipeline using NLTK/spaCy or Ollama."""
import logging
from typing import Dict, List, Any

logger = logging.getLogger("civic_sentinel.nlp")

class NLPPipeline:
    def __init__(self):
        self.spacy_loaded = False
        self.nltk_loaded = False
        # Try to import optionally (heavy deps)
        try:
            import spacy  # noqa
            self.spacy_loaded = True
        except ImportError:
            logger.warning("spacy not installed; NLP will use simple heuristic")
        try:
            import nltk  # noqa
            self.nltk_loaded = True
        except ImportError:
            logger.warning("nltk not installed; NLP will use simple heuristic")

    def process(self, text: str) -> Dict[str, Any]:
        """Run NLP on text; return summary and entities."""
        # Summary: first 200 chars for demo
        summary = text[:200] if text else "No content"

        entities: List[dict] = []
        if self.spacy_loaded:
            # TODO: load model and extract entities
            entities = [{"text": "Example", "label": "PERSON"}]
        else:
            # Very simple heuristic: capitalized words
            import re
            words = re.findall(r'\b[A-Z][a-z]{2,}\b', text)
            entities = [{"text": w, "label": "UNKNOWN"} for w in set(words[:10])]

        return {
            "summary": summary,
            "entities": entities,
            "language": "en",
        }
