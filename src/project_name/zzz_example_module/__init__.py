"""
Module initialization.
Handles path setup and common imports for all files in this folder.
"""

import sys
from pathlib import Path

# Set up project_root once for this subfolder
# This subfolder is 4 levels deep from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Import and re-export common modules for this folder
try:
    from src.project_name.logging_setup import logger
    from src.project_name.key_cert_load import llm_gateway_key, CERT_PATH
except ImportError:
    logger = None
    llm_gateway_key = None
    CERT_PATH = None

# Make these available to other modules in this package
__all__ = ['PROJECT_ROOT', 'logger', 'llm_gateway_key', 'CERT_PATH']
