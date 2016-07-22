import sys
from langid import arguments, model, output


def main():
    """
    Language identification main script.

    This script identifies the language of a text.
    The text is read from STDIN.
    The language is displayed on STDOUT using a 2 letter code (e.g. 'en', 'de')
    """
    args = arguments.parse_args()
    text = sys.stdin.read()
    result = model.run(text, args)
    output.display(result, args)


if __name__ == "__main__":
    main()
