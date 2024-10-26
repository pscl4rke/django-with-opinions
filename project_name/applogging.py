

import logging


def set_up_basic_configuration() -> None:
    # E.g. for journald
    #logformat = "%(name)s:%(lineno)s %(levelname)s %(message)s"
    # E.g. for files
    #logformat = "%(asctime)s %(logwrapreqidshort)s %(logwrapprefix)s %(name)s:%(lineno)s %(levelname)s %(message)s"
    logging.basicConfig(
        level=0,
        #stream=sys.stdout,  # Use stdout (not stderr) for better cronjob->syslog support
        #format=logformat,
        #datefmt="%Y-%m-%d %H:%M:%S",
    )


def set_up_various_levels() -> None:
    # Note django.server is really only for "manage.py runserver"
    logging.getLogger("django.template").setLevel("INFO")
    logging.getLogger("django.request").setLevel("ERROR")  # 404s are warnings
    logging.getLogger("django.utils.autoreload").setLevel("INFO")



def initialise() -> None:
    set_up_basic_configuration()
    set_up_various_levels()
