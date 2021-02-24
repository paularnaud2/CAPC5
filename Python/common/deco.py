import os
import traceback
import conf_main as cfg

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

    if hasattr(cfg, 'DEBUG'):
        if cfg.DEBUG:
            return new
        else:
            return f
    return new
