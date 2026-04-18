"""MarkItDown - Convert various file formats to Markdown.

A fork of microsoft/markitdown with additional features and improvements.

Note: Personal fork - experimenting with custom converters and output formatting.
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__version__ = "0.1.0"
__author__ = "personal fork of microsoft/markitdown"
__all__ = ["MarkItDown", "DocumentConverter", "ConversionResult"]
