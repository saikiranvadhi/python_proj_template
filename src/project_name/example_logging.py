"""
Example to demonstrate logging setup in the main package.
"""
def setup_environment():
    """Setup the environment and import required modules."""
    import importlib.util
    from pathlib import Path
    
    setup_path = Path(__file__).parent / "_standalone_setup.py"
    spec = importlib.util.spec_from_file_location("_standalone_setup", setup_path)
    setup = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(setup)
    
    return setup.llm_gateway_key, setup.CERT_PATH, setup.logger

def main():
    # Setup environment
    api_key, cert_path, logger = setup_environment()
    
    logger.info("Starting example logging demonstration")
    
    # Log various levels
    logger.debug("This is a DEBUG message - usually for development")
    logger.info("This is an INFO message - general information")
    logger.warning("This is a WARNING message - something to pay attention to")
    logger.error("This is an ERROR message - something went wrong")
    logger.critical("This is a CRITICAL message - severe error")
    
    logger.info("Example logging demonstration completed")

if __name__ == "__main__":
    main()
