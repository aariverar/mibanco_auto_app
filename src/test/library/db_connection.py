#import cx_Oracle
import oracledb
import os
import configparser

def connectionBD():
    try:
        config = configparser.ConfigParser()
        config.read('database.properties')
        port= config.get('Database', 'puerto')
        service_Name = config.get('Database', 'service_name')
        hostname = config.get('Database', 'hostname')
        username= config.get('Database', 'name_username')
        password = config.get('Database', 'name_password')

        # Conexión a la base de datos usando un alias
        oracledb.init_oracle_client(lib_dir=r"D:/instantclient_23_5")
        dsn_tns= oracledb.makedsn(hostname,port,service_name=service_Name)
        #dsn_tns= oracledb.makedsn('10.100.50.7',1534,service_name='tpzqa06.domibco.com.pe')
        connection = oracledb.connect(user=username, password=password, dsn=dsn_tns, disable_oob=True)
        #connection = oracledb.connect(user=p_usuarioBD, password=p_contrasenaBD, dsn=dsn_tns, disable_oob=True)
        print("[LOG] Se ejecutó correctamente la conexión a la BD")
        return connection
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error al conectar: {error.message}")
        return None
        # Aquí puedes manejar el error como necesites


def consultaCliente(id_Cliente, connection):
    try:
        cursor = connection.cursor()
        query = "SELECT C.C0902 AS COD_CLIENTE_BD, C.C1040 AS COD_TIPO_CLIENTE,C.C1000 AS NOMBRE_RSOCIAL,   C.C1023 AS FECHA_CREACION,    P.C1431 AS TIPO_DOC,       P.C1432 AS NRO_DOCUMENTO,       P.C1437 AS TIPO_CLIENTE FROM edyficar.CL_CLIENTES C LEFT JOIN edyficar.cl_clientpersona P ON P.C1430 = C.C0902 WHERE C.C0902 IN (:id_Cliente)"
        cursor.execute(query,id_cliente=id_Cliente)

        for row in cursor:
            print(row)
        return row
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error al conectar: {error.message}")
    finally:
        cursor.close()


# bdconec = conecction()
# consultaCliente(10440504,bdconec)
# consultaCliente(10440505,bdconec)