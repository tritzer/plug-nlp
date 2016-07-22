import json
import sys


def csv_format(result):
    """
    Writes the language identification result in CSV format lang_code,text.

    Example:
        en,this is an English text

    :param result: the language identification result
    """
    lang_code, text = result

    sys.stdout.write("{},{}".format(lang_code, text))


def json_format(result):
    """
    Writes the language identification result in JSON format.

    Example:
        {
            'lang_code': 'en',
            'text': 'This is an English text'
        }

    :param result: the language identification result
    :param result:
    :return:
    """
    lang_code, text = result
    result = {'lang_code': lang_code, 'text': text.strip()}

    sys.stdout.write(json.dumps(result))


def get_formatter(format):
    """
    Retrieves the proper formatter,
    according to the format command line parameter.

    :param format: the format command line parameter
    :return: the proper formatter function
    """
    if format == 'csv':
        return csv_format
    elif format == 'json':
        return json_format


def display(result, args):
    """
    Displays the language identification results
    according to the format defined by command line arguments.

    :param result:  the language identification results.
    :param args:    the command line arguments.
    """
    formatter = get_formatter(args.format)
    formatter(result)
