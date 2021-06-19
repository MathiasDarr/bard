import os


APP_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = bool(os.getenv("DAKOBED_DEBUG", True))
# Profile requests
PROFILE = bool(os.getenv("DAKOBED_PROFILE", False))
# Propose HTTP caching to the user agents.
CACHE = bool(os.getenv("BARD_CACHE", not DEBUG))
# Puts the system into read-only mode and displays a warning
MAINTENACE = bool(os.getenv("BARD_MAINTENANCE", False))
# Unit test context
TESTING = False


# GENERAL INSTANCE INFORMATION

APP_TITLE = os.getenv("DAKOBED_APP_TITLE", "Dakobed Bard")
APP_NAME = os.getenv("BARD_APP_NAME", "bard")
APP_UI_URL = os.getenv("BARD_UI_URL","http://localhost:8080")
APP_FAVICON = os.getenv("BARD_FAVICON", "/static/favicon.png")
APP_LOGO = os.getenv("DAKOBED_LOGO","/static/logo.png")
APP_LOGO_AR = os.getenv("BARD_LOGO_AR", APP_LOGO)



DATABASE_URI = 'postgresql://bard:bard@postgres:5432/bard'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALEMBIC_DIR = os.path.join(APP_DIR, "migrate")

SYSTEM_USER = os.getenv("BARD_SYSTEM_USER", "system:bard")




# Content processing options
DEFAULT_LANGUAGE = os.getenv("BARD_DEFAULT_LANGUAGE", "en")

# Document processing pipeline
INGEST_PIPELINE = ["analyze"]
