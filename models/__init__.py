"""
Spamlyser Pro Models Package
This package contains all the model-related functionality for SMS threat detection.
"""

from .batch_processor import BatchProcessor
from .calibration import ConfidenceCalibrator
from .custom_rules_manager import (
    check_custom_rules,
    load_custom_rules,
    save_custom_rules,
)
from .export_feature import export_results_button
from .simple_explainer import SPAM_KEYWORDS, SimpleExplainer
from .model_comparator import compare_predictions, agreement_score
from .storage_manager import StorageManager, default_json_validator
from .threat_analyzer import (
    THREAT_CATEGORIES,
    classify_threat_type,
    get_threat_specific_advice,
)
from .word_analyzer import WordAnalyzer

__all__ = [
    "SPAM_KEYWORDS",
    "THREAT_CATEGORIES",
    "BatchProcessor",
    "ConfidenceCalibrator",
    "SimpleExplainer",
    "StorageManager",
    "WordAnalyzer",
    "agreement_score",
    "check_custom_rules",
    "classify_threat_type",
    "compare_predictions",
    "default_json_validator",
    "export_results_button",
    "get_threat_specific_advice",
    "load_custom_rules",
    "save_custom_rules",
]
