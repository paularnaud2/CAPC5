import sys
import common as com
import reqlist.gl as gl
import reqlist.log as log


def restart():
    file_list = com.get_file_list(gl.TMP_PATH)
    a = len(file_list)
    if a == 0:
        return

    s = "Traitement en cours détecté. Tuer ? (o/n)"
    if com.log_input(s) == 'o':
        com.delete_folder(gl.TMP_PATH)
        return
    return


def gen_group_list():
    com.log("Construction des groupes d'éléments...")
    elt_list = prepare_elt_list(gl.ar_in)

    i = 0
    cur_elt_list = []
    group_list = []
    for elt in elt_list:
        cur_elt_list.append(elt)
        i += 1
        if len(cur_elt_list) % gl.NB_MAX_ELT_IN_STATEMENT == 0:
            grp = gen_group(cur_elt_list)
            group_list.append(grp)
            cur_elt_list = []
    if len(cur_elt_list) > 0:
        grp = gen_group(cur_elt_list)
        group_list.append(grp)

    gl.group_list = group_list
    log.gen_group_list(elt_list, group_list)


def gen_group(elt_list):
    in_st = "('" + elt_list[0]
    for elt in elt_list[1:]:
        in_st += "', '" + elt
    in_st += "')"

    return in_st


def set_query_var(query_file):
    query = com.read_file(query_file)
    query = query.strip('\r\n;')
    query = com.replace_from_dict(query, gl.VAR_DICT)
    gl.query_var = query
    s = "Requête modèle :\n{}\n;"
    com.log_print(s.format(gl.query_var))


def prepare_elt_list(array_in):
    # tri et suppression des doublons

    elt_list = str_handle(array_in)
    elt_set = set()
    for elt in elt_list:
        elt_set.add(elt)

    elt_list = []
    for elt in elt_set:
        elt_list.append(elt)
    elt_list.sort()

    bn = com.big_number(len(elt_list))
    s = f"Liste des éléments préparée, elle contient {bn} éléments."
    com.log(s)

    return elt_list


def str_handle(array_in):
    if not com.has_header(array_in):
        s = "Attention il semble ne pas y avoir de header dans l'entrant"
        s += f" (premier élément : {array_in[0]}) Continuer ? (o/n)"
        if com.log_input(s) != 'o':
            sys.exit()

    if gl.IN_FIELD_NB != 1:
        s = "Attention les requêtes se feront sur le {}ème champ "
        s += "du tableau d'entrée. Continuer ? (o/n)"
        s = s.format(gl.IN_FIELD_NB)
        if com.log_input(s) != 'o':
            sys.exit()

    elt_list = [elt[gl.IN_FIELD_NB - 1] for elt in array_in[1:]]

    return elt_list
