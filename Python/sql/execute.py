import common as com
import sql.gl as gl

from sql.init import init
from sql.init import init_params
from sql.connect import connect
from sql.functions import get_final_script


@com.log_exeptions
def execute(**params):
    com.log('[sql] execute')
    init_params(params)
    init()
    script = get_final_script(gl.SCRIPT_FILE)
    cnx = connect(ENV=gl.ENV, BDD=gl.BDD)
    c = cnx.cursor()
    if gl.PROC:
        com.log("Execution de la procédure :")
        com.log_print(script)
        c.execute(script)
        com.log("Procédure executée")
    else:
        command_list = script.split(';')
        for command in command_list:
            com.log("Execution de la commande :")
            com.log_print(command)
            c.execute(command)
            com.log("Commande executée")
    c.close()
    cnx.commit()
    cnx.close()
    com.log_print()
