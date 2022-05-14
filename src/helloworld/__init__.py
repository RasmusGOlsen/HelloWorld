import sys
import logging

__version__ = "0.0.1"
__author__ = "Rasmus Olsen"
__email__ = "zordid+github@gmail.com"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

_LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s %(message)s'

_VERBOSITY_LEVELS = {
    1: logging.INFO,
    2: logging.DEBUG,
}


def configure_logging(verbosity, filename=None, logformat=_LOG_FORMAT):
    """
    Configure logging for the application.
    """
    if not verbosity:
        return

    verbosity = min(verbosity, max(_VERBOSITY_LEVELS))
    log_level = _VERBOSITY_LEVELS[verbosity]

    if not filename or filename in ("stderr", "stdout"):
        fileobj = getattr(sys, filename or "stderr")
        handler_cls = logging.StreamHandler
    else:
        fileobj = filename
        handler_cls = logging.FileHandler

    handler = handler_cls(fileobj)
    handler.setFormatter(logging.Formatter(logformat))
    logger.addHandler(handler)
    logger.setLevel(log_level)
    logger.debug(
        "Added a %s logging handler to logger root at %s", filename, __name__
    )
