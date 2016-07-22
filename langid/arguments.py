import argparse


def parse_args():
    """
    Parse the command line arguments.
    """
    description = """Identify the language of a text.
The text is read from STDIN and the output is displayed on STDOUT.
"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--format', default='csv', choices=['csv', 'json'], help='Format of the output')

    return parser.parse_args()
