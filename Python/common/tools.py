from . import g
from .log import log


def send_notif(msg, package, duration=0, cond=True):

    if duration != 0:
        duration = duration / 1000
        if duration < g.MIN_DUR_NOTIF_TRIGGER:
            return

    if not cond:
        return

    try:
        from win10toast import ToastNotifier
    except ModuleNotFoundError:
        s = "Échec de l'envoi de la notification windows. Le module win10toast \
        n'est pas installé."

        log.log(s)
        return

    toaster = ToastNotifier()
    toaster.show_toast("Python - " + package, msg, duration=10, threaded=True)
    log("Notification Windows envoyée")


def split_array(array_in, max_elt):
    array_out = []
    cur_array = array_in[0:max_elt]
    i = 0
    while cur_array != []:
        i += 1
        array_out.append(cur_array)
        cur_array = array_in[max_elt * i:max_elt * (i + 1)]

    return array_out


def print_list(list):
    for elt in list:
        print(elt)


def print_array(array, nb_tab=0):
    for elt in array:
        print(elt, nb_tab)


def print_dict(dict):
    for key in dict:
        print(f'{key} : {dict[key]}')
