from configparser import ConfigParser
import psycopg2


def read_config_mail(filename="settings.ini", section="mail"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    mail = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            mail[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return mail
