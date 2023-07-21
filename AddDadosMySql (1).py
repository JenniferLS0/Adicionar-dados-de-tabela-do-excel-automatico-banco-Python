# Script para inserir dados em uma tabela do MySql
import pandas as pd
import numpy as np
from mysql.connector import Error
import mysql.connector
from sqlalchemy import create_engine

# String padrão de conectividade do DB


def Con_SQL(user, user_pass, server, bd):
    global cursor
    engineAlchemy = create_engine(
        "mysql+pymysql://"+user+":"+user_pass+"@"+server+"/"+bd+"?charset=utf8mb4")
    engine = mysql.connector.connect(
        user=user, password=user_pass, host=server, database=bd, auth_plugin='mysql_native_password')
    return engine, engineAlchemy


# Dados do BD    
BD_USER = 'root'
BD_USER_PASS = 'portal_tsr_dev'
BD_SERVER = 'localhost'
BD_BD = 'portaltsr_dev'

# Importando a tabela do excel para o py
df = pd.read_excel("Clientes ativos x Grupos Kaizala.xlsx")

# Conexão com o banco
BD_Sys = Con_SQL(BD_USER, BD_USER_PASS, BD_SERVER, BD_BD)

# função para dar update no banco
for index, row in df.iterrows():
    atualizar_ = """update portaltsr_dev.clientes set `GrupoTivit` ='{0}', `GrupoCliente`='{1}' where `Nome` ='{2}'""".format(row['GRUPO TIVIT'],row['GRUPO CLIENTE'],row['CLIENTES ATIVOS - PORTAL'])

    print(atualizar_)
    cursor = BD_Sys[0].cursor()
    cursor.execute(atualizar_)
    BD_Sys[0].commit()
    cursor.close()
