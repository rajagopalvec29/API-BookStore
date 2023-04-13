import cx_Oracle
from cx_Oracle import Error
import configparser
import os
os.environ['PATH'] = "E:\\instantclient_21_9"


def getConfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Admin\\PycharmProjects\\API_BookStore\\Utilities\\properties.ini")
    return config



def getDBConnect():
    DB_config = {'user': getConfig()['SQL']['user'],
                 'password': getConfig()['SQL']['password'],
                 'dsn': getConfig()['SQL']['dsn']}
    try :
        con = cx_Oracle.connect(**DB_config)
        return con
    except Error as e:
        print(e)


def getQuery(query):
    con = getDBConnect()
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchone()
    con.close()
    return res

