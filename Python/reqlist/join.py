import sys
import common as com
import reqlist.gl as gl


def join_arrays(ar_left_in, ar_right_in):
    com.log("Jointure des deux tableaux (initialisation)")
    check_void_right_array(ar_right_in)
    com.log("Préparation du tableau de gauche...")
    (ar_left, first_line_l) = prepare_array(ar_left_in)
    com.save_csv(ar_left, gl.OUT_LEFT)
    log_prepare(gl.OUT_LEFT, com.big_number(len(ar_left)))

    com.log("Préparation du tableau de droite...")
    (ar_right, first_line_r) = prepare_array(ar_right_in)
    com.save_csv(ar_right, gl.OUT_RIGHT)
    log_prepare(gl.OUT_RIGHT, com.big_number(len(ar_right)))

    com.log("Jointure des deux tableaux en cours...")
    init_while_join(first_line_l, first_line_r)
    while gl.bools["end_left"] is False or gl.bools["end_right"] is False:
        (pdl_l, pdl_r) = update_pdl(ar_left, ar_right)
        pdl_l = compare_inf(pdl_l, pdl_r, ar_left)
        (pdl_l, pdl_r) = compare_sup(pdl_l, pdl_r, ar_left, ar_right)
        pdl_r = compare_equal(pdl_l, pdl_r, ar_left, ar_right)
        if incr_c_l(ar_left):
            break
    s = "Jointure effecutée. Le tableau de sortie comporte {}"
    s += " lignes (en-tête incluse)."
    com.log(s.format(com.big_number(len(gl.out_array))))


def prepare_array(array_in):
    # tri et suppression de doublons

    array_out = array_in
    if isinstance(array_out[0], str):
        array_out = [[elt] for elt in array_out]
    first_line = array_out[0]
    check_first_line(first_line)
    del array_out[0]
    array_out = del_dup(array_out)

    return (array_out, first_line)


def log_prepare(ar, bn_ar):
    n_dup = len(gl.dup_list)
    bn_dup = com.big_number(n_dup)
    s = "Tableau préparé et enregistré sous '{}'"
    s += " ({} lignes, {} doublons écartés)"
    com.log(s.format(ar, bn_ar, bn_dup))

    if n_dup > 0:
        s = "Exemples de doublons (limités à {}) :"
        com.log(s.format(gl.MAX_DUP_PRINT))
        com.log_array(gl.dup_list[:gl.MAX_DUP_PRINT])


def check_first_line(first_line):
    if is_elt(first_line[0]):
        s = "Le tableau à préparer doit contenir une en-tête."
        s += " Arrêt du traitement."
        com.log(s)
        sys.exit()


def check_void_right_array(ar_right_in):
    if len(ar_right_in) == 1:
        com.log("Le tableau de droite est vide. Arrêt du traitement.")
        sys.exit()


def init_while_join(first_line_l, first_line_r):
    gl.out_array = []
    gl.old_pdl_l = 'old_pdl_init'
    gl.blank_right_row = ['' for elt in first_line_r[1:]]
    gl.out_array.append(first_line_l + first_line_r[1:])
    gl.counters["c_l"] = 0
    gl.counters["c_r"] = 0
    gl.counters["out"] = 0
    gl.bools["end_left"] = False
    gl.bools["end_right"] = False


def update_pdl(ar_left, ar_right):
    pdl_l = ar_left[gl.counters["c_l"]][0]
    if pdl_l == gl.old_pdl_l:
        # le curseur c_e_r permet de sauvegarder la position
        # du curseur droit pour le premier cas de pdl egal
        # cela permet d'y revenir lorsque l'on a parcouru
        # les pdl égaux à gauche
        gl.counters["c_r"] = gl.counters["c_e_r"]

    pdl_r = ar_right[gl.counters["c_r"]][0]

    return (pdl_l, pdl_r)


def compare_inf(pdl_l, pdl_r, ar_left):
    while pdl_l < pdl_r:
        out_line = ar_left[gl.counters["c_l"]] + gl.blank_right_row
        gl.out_array.append(out_line)
        gl.counters["out"] += 1
        debug('compare_inf', pdl_l, pdl_r, out_line)
        if incr_c_l(ar_left):
            break
        pdl_l = ar_left[gl.counters["c_l"]][0]

    return pdl_l


def compare_sup(pdl_l, pdl_r, ar_left, ar_right):
    while pdl_l > pdl_r:
        out_line = ar_left[gl.counters["c_l"]] + gl.blank_right_row
        gl.out_array.append(out_line)
        gl.counters["out"] += 1
        debug('compare_sup', pdl_l, pdl_r, out_line)
        if not gl.bools["end_right"]:
            if incr_c_r(ar_right):
                break
            pdl_r = ar_right[gl.counters["c_r"]][0]
        else:
            if incr_c_l(ar_left):
                break
            pdl_l = ar_left[gl.counters["c_l"]][0]

    return (pdl_l, pdl_r)


def compare_equal(pdl_l, pdl_r, ar_left, ar_right):
    gl.counters["c_e_r"] = gl.counters["c_r"]
    while pdl_l == pdl_r:
        out_line = ar_left[gl.counters["c_l"]] + ar_right[
            gl.counters["c_r"]][1:]
        gl.out_array.append(out_line)
        gl.counters["out"] += 1
        debug('compare_equal', pdl_l, pdl_r, out_line)
        if incr_c_r(ar_right):
            break
        pdl_r = ar_right[gl.counters["c_r"]][0]
        gl.old_pdl_l = pdl_l

    return pdl_r


def incr_c_l(ar_left):
    # incrémente le curseur de gauche et vérifie si l'on arrive
    # à la fin du tableau.
    # Dans ce cas on positionne le compteur à -1

    gl.counters["c_l"] += 1
    if gl.counters["c_l"] == len(ar_left):
        gl.counters["c_l"] -= 1
        gl.bools["end_left"] = True
        return True
    return False


def incr_c_r(ar_right):
    # incrémente le curseur de droit et vérifie si l'on arrive
    # à la fin du tableau.
    # Dans ce cas on positionne le compteur à -1

    gl.counters["c_r"] += 1
    if gl.counters["c_r"] == len(ar_right):
        gl.counters["c_r"] -= 1
        gl.bools["end_right"] = True
        return True
    return False


def debug(s, pdl_l, pdl_r, out_line):
    if not gl.DEBUG_JOIN:
        return

    print(s)
    print([gl.counters["c_l"] + 2, gl.counters["c_r"] + 2])
    print([pdl_l, pdl_r])
    print(out_line)
    com.log_array(gl.out_array)
    com.log_print()
    if pdl_l == '01103762594604':
        print(pdl_l)


def del_dup(array_in):
    # suppression des doublons

    array_out = array_in
    array_out.sort()
    dup_list = []
    gl.counters["dup"] = 0
    old_line = array_out[0]
    i = 1
    for line in array_out[1:]:
        if line == old_line:
            dup_list.append(array_out[i])
            del array_out[i]
        else:
            old_line = line
            i += 1

    gl.counters["dup"] = len(dup_list)
    if len(dup_list) > 0:
        gl.dup_list = del_dup(dup_list)
    else:
        gl.dup_list = []

    return array_out


def is_elt(str_in):
    a = str_in[0].isdigit()
    b = len(str_in) >= 2
    return a and b
