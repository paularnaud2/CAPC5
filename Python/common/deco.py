import os
import traceback

from . import g
from .log import log
from .log import log_print


def log_exeptions(f):
    def new(*arg, **kwargs):
        try:
            return f(*arg, **kwargs)
        except Exception:
            with g.verrou:
                s = "Une erreur est survenue :\n"
                s += traceback.format_exc()
                log(s)
                log_print("Arrêt du traitement")
                os._exit(1)

    if g.DEBUG:
        return f
    else:
        return new
