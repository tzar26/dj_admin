from settings import *

import os, sys
sys.path.insert(1, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


DEBUG=True
TEMPLATE_DEBUG=DEBUG

POLL_LENGTH = 10
DUPLICATE_QUESTION_RETRY_ABORT = 10
SESSION_EXPIRED_MINUTES = 30