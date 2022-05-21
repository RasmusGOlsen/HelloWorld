import logging

from helloworld import configure_logging
from .arguments import parse_arguments


logger = logging.getLogger(__name__)


def main():
    """
    The main entry point for the application.
    """
    args = parse_arguments()
    configure_logging(args.verbose, args.logfile)
    logger.debug(f"Print Hello {args.name}")
    logger.info(f"Print Hello {args.name}")
    print(f"Hello {args.name}!")
