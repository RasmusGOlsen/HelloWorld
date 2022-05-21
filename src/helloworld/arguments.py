import argparse

from helloworld import __version__


def parse_arguments():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='A simple Hello World program.'
    )
    parser.add_argument(
        'name',
        help='The name to greet.',
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}',
        help='Print the version number and exit.',
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=0,
        action="count",
        help="Print more information about what is happening. "
             "This option is repeatable and will increase verbosity each "
             "time it is repeated.",
    )
    parser.add_argument(
        '--logfile',
        metavar='FILE',
        default=None,
        help='The file to log to.',
    )
    return parser.parse_args()
