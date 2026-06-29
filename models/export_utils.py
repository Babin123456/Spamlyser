"""
Reusable model export utilities for Spamlyser Pro.

Provides helper functions for exporting HuggingFace models to ONNX and
TorchScript formats, with proper error handling and logging.
"""

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def export_to_onnx(
    model_id: str,
    output_path: str = "model.onnx",
    seq_len: int = 8,
    opset: int = 14,
) -> Optional[Path]:
    """Export a HuggingFace model to ONNX format.

    Args:
        model_id: HuggingFace model name.
        output_path: Destination path for the ONNX file.
        seq_len: Dummy input sequence length.
        opset: ONNX opset version.

    Returns:
        Path to the exported file, or None on failure.
    """
    import torch
    from transformers import AutoModelForSequenceClassification

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    try:
        model = AutoModelForSequenceClassification.from_pretrained(model_id)
        model.eval()
        dummy = torch.randint(0, 100, (1, seq_len))

        with torch.no_grad():
            torch.onnx.export(
                model,
                dummy,
                str(output),
                input_names=["input_ids"],
                output_names=["output"],
                dynamic_axes={
                    "input_ids": {0: "batch_size", 1: "sequence_length"},
                    "output": {0: "batch_size"},
                },
                opset_version=opset,
            )
        logger.info("ONNX export completed: %s", output)
        return output
    except Exception as e:
        logger.error("ONNX export failed: %s", e)
        return None


def export_to_torchscript(
    model_id: str,
    output_path: str = "model.pt",
    seq_len: int = 8,
) -> Optional[Path]:
    """Export a HuggingFace model to TorchScript format.

    Args:
        model_id: HuggingFace model name.
        output_path: Destination path for the TorchScript file.
        seq_len: Dummy input sequence length.

    Returns:
        Path to the exported file, or None on failure.
    """
    import torch
    from transformers import AutoModelForSequenceClassification

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    try:
        model = AutoModelForSequenceClassification.from_pretrained(model_id)
        model.eval()
        dummy = torch.randint(0, 100, (1, seq_len))

        with torch.no_grad():
            traced = torch.jit.trace(model, dummy)
            traced.save(str(output))
        logger.info("TorchScript export completed: %s", output)
        return output
    except Exception as e:
        logger.error("TorchScript export failed: %s", e)
        return None
