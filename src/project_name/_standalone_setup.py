"""
Standalone setup utility for when files are run directly (non-module mode).

This file handles ALL import logic - tries relative imports first, falls back to absolute imports.
Other files in this subfolder can simply import from this file.
"""

import sys
from pathlib import Path

# Global variables to store the imports once loaded
_llm_gateway_key = None
_CERT_PATH = None
_logger = None
_imports_loaded = False


def _load_imports():
    """
    Internal function to load imports with fallback logic.
    Tries relative imports first, then falls back to absolute imports.
    """
    global _llm_gateway_key, _CERT_PATH, _logger, _imports_loaded
    
    if _imports_loaded:
        return
    
    try:
        # Try relative import first (when run as module)
        from . import llm_gateway_key, CERT_PATH, logger
        _llm_gateway_key = llm_gateway_key
        _CERT_PATH = CERT_PATH
        _logger = logger
    except ImportError:
        # Fallback for direct execution - use absolute imports with sys.path setup
        # Calculate project root from this file's location
        PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

        # Add to sys.path if not already there
        if str(PROJECT_ROOT) not in sys.path:
            sys.path.append(str(PROJECT_ROOT))

        # Import the required modules
        from src.project_name.key_cert_load import llm_gateway_key, CERT_PATH
        from src.project_name.logging_setup import logger

        _llm_gateway_key = llm_gateway_key
        _CERT_PATH = CERT_PATH
        _logger = logger
    
    _imports_loaded = True


# Load imports immediately when this module is imported
_load_imports()

# Export the variables directly so they can be imported
logger = _logger
llm_gateway_key = _llm_gateway_key
CERT_PATH = _CERT_PATH
