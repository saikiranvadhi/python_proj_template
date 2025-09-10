import os
import sys
import dotenv
from pathlib import Path

# Get project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


# Try module import for logging, fall back to absolute import
try:
    from .logging_setup import setup_logger
    logger = setup_logger()
except ImportError:
    from project_name.logging_setup import setup_logger
    logger = setup_logger()

def load_llm_gateway_key():
    """Load the LLM Gateway API key from environment variables."""
    dotenv.load_dotenv()
    return os.getenv("LLM_GATEWAY_KEY")

def setup_certificate_path():
    """Setup the certificate path and environment variables."""
    cert_path = str(PROJECT_ROOT / "certs" / "ca-bundle.crt")
    os.environ['SSL_CERT_FILE'] = cert_path
    os.environ['REQUESTS_CA_BUNDLE'] = cert_path
    logger.debug(f"Certificate bundle path: {cert_path}")
    return cert_path

def get_project_root():
    """Get the project root directory."""
    return PROJECT_ROOT

# Load configuration on module import
llm_gateway_key = load_llm_gateway_key()
CERT_PATH = setup_certificate_path()

logger.debug(f"Project root directory: {PROJECT_ROOT}")