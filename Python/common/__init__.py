from .log import log
from .log import init_log
from .tools import send_notif


def list_print(list):
    for elt in list:
        print(elt)


def array_print(array, nb_tab=0):
    for elt in array:
        print(elt, nb_tab)


def dict_print(dict):
    for key in dict:
        print(f'{key} : {dict[key]}')
