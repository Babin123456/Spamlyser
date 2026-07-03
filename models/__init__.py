"""
Spamlyser Pro Models Package
This package contains all the model-related functionality for SMS threat detection.
"""

# Import benchmark helpers from the top-level benchmarks package (optional).
try:
    from benchmarks.benchmark_runner import (
        confidence_distribution,
        latency_benchmark,
        run_all,
        summary,
    )
except ImportError:
    pass

from .batch_processor import BatchProcessor
from .calibration import ConfidenceCalibrator
from .custom_rules_manager import (
    check_custom_rules,
    load_custom_rules,
    save_custom_rules,
)
from .export_feature import export_results_button
from .simple_explainer import SPAM_KEYWORDS, SimpleExplainer
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
    "check_custom_rules",
    "classify_threat_type",
    "confidence_distribution",
    "default_json_validator",
    "export_results_button",
    "get_threat_specific_advice",
    "latency_benchmark",
    "load_custom_rules",
    "run_all",
    "save_custom_rules",
    "summary",
]
