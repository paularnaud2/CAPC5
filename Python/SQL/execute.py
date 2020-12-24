import common as com
import SQL.gl as gl

from SQL.init import init
from SQL.init import init_params
from SQL.connect import connect
from SQL.functions import get_final_script


@com.log_exeptions
def execute(**params):
    init_params(params)
    init()
    script = get_final_script(gl.SCRIPT_FILE)
    cnx = connect(BDD=gl.BDD, ENV=gl.ENV)
    c = cnx.cursor()
    if gl.PROC:
        com.log("Execution de la procédure :")
        com.print_com(script)
        c.execute(script)
        com.log("Procédure executée")
    else:
        command_list = script.split(';')
        for command in command_list:
            com.log("Execution de la commande :")
            com.print_com(command)
            c.execute(command)
            com.log("Commande executée")
    c.close()
    cnx.commit()
    cnx.close()
