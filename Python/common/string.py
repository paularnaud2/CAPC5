from math import floor
from time import time


def get_duration_string(duration_ms):
    if duration_ms >= 1000:
        duration_s = duration_ms/1000
        if duration_s > 60:
            duration_m = duration_s//60
            duration_s = duration_s % 60
            out = str(floor(duration_m)) + " minutes et "
            + str(floor(duration_s)) + " secondes"
            return(out)
        out = str(duration_s) + " secondes"
        return(out)
    out = str(duration_ms) + " ms"
    return(out)


def get_duration_ms(start_time, end_time=''):
    if end_time == '':
        end_time = time()

    duration = floor((end_time - start_time) * 1000)

    return duration


def big_number(str_in):
    s = str(str_in)
    position = len(s)
    counter = 0
    out = ''
    while position != 0:
        counter += 1
        position -= 1
        out = s[position] + out
        if counter % 3 == 0 and position != 0:
            out = " " + out
    return(out)


def reverse_string(str_in):
    str_out = ''
    for i in str_in:
        str_out = i + str_out

    return str_out
