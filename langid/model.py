import pycld2


def run(text, args):
    """
    Run the language identification module.

    :param text: the input text
    :param args: the command line arguments
    :return: a tuple in the form (language_code, text)
    """
    _, _, languages = pycld2.detect(text.strip().encode('utf-8'))

    if len(list(languages)) > 0:
        language = languages[0]
        _, lang_code, _, _ = language
    else:
        lang_code = 'un'

    return lang_code, text
