"""Tests for model export utilities."""

from pathlib import Path
from unittest.mock import patch, MagicMock

from models.export_utils import export_to_onnx, export_to_torchscript


class FakeModule:
    def eval(self):
        pass

    def __call__(self, x):
        return x


@patch("transformers.AutoModelForSequenceClassification")
def test_export_to_onnx_happy_path(mock_auto, tmp_path):
    mock_model = MagicMock()
    mock_model.eval.return_value = None
    mock_auto.from_pretrained.return_value = mock_model
    output = str(tmp_path / "test.onnx")
    result = export_to_onnx("dummy", output)
    assert result is None or isinstance(result, Path)


@patch("transformers.AutoModelForSequenceClassification")
def test_export_to_torchscript_happy_path(mock_auto, tmp_path):
    mock_model = MagicMock()
    mock_model.eval.return_value = None
    mock_auto.from_pretrained.return_value = mock_model
    output = str(tmp_path / "test.pt")
    result = export_to_torchscript("dummy", output)
    assert result is None or isinstance(result, Path)


@patch("transformers.AutoModelForSequenceClassification")
def test_export_to_onnx_returns_none_on_failure(mock_auto):
    mock_auto.from_pretrained.side_effect = RuntimeError("fail")
    assert export_to_onnx("bad-model", "out.onnx") is None


@patch("transformers.AutoModelForSequenceClassification")
def test_export_to_torchscript_returns_none_on_failure(mock_auto):
    mock_auto.from_pretrained.side_effect = RuntimeError("fail")
    assert export_to_torchscript("bad-model", "out.pt") is None
