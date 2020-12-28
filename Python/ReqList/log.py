from common import com


def log_get_sql_array_finish(th_nb):
    cur_n_rows = 1
    if th_nb == 0:
        s_th = ''
    else:
        s_th = " pour le pool No.{}".format(th_nb)
    if cur_n_rows > 0:
        bn = com.big_number(cur_n_rows)
        s = "Résultat récupéré{} ({} lignes exportées)"
        s = s.format(s_th, bn)
        com.log(s)
    else:
        com.log("Aucune ligne récupéré{}".format(s_th))
