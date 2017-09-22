import os
import sys
sys.path.append(os.path.dirname( os.path.abspath( __file__ ))+"/module")
import argparse
from connMySQL import *
from connOracle import *

global nomTabla
global ptrDB

######### VIEW SHELL ###########################

class ViewTableWithFormat(object):
    """docstring for ViewTableWithFormat"""
    def __init__(self, arg):
        super(ViewTableWithFormat, self).__init__()
        self.arg = arg
    
    def __call__(self):
        pass


############## CONEXIONES A LAS DB'S ###############    
# CREAR UN MODULO PROPIO PARA DISTINTAS DBS
def registrarDB(dbuser,dbpass,dbname):
    if ptrDB == 'orc':
        CON = ConnectionOracle(dbuser,dbpass,dbname)
    if ptrDB == 'mys':
        CON = ConnectionMySQL(dbuser,dbpass,dbname)
    
    return CON


######################## MAIN #######################
parser = argparse.ArgumentParser(description='Mi Primer Hola Mundo')

subparsers = parser.add_subparsers(help='sub-command help',dest='subparser_name')

parse_orc = subparsers.add_parser('orc')
parse_orc.add_argument('-js',"--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_orc.add_argument('-txt',"--extxt", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_orc.add_argument('-csv',"--excsv",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")

parse_mys = subparsers.add_parser('mys')
parse_mys.add_argument('-js',"--exjson",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_mys.add_argument('-txt',"--extxt",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_mys.add_argument('-csv',"--excsv",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")

args = parser.parse_args()

#print('WHAT SAID ',args.json)
#print(type(args.json))
#print(args.subparser_name)
if args.subparser_name == 'orc':
    ptrDB = 'orc'
    if args.extxt:
      nomTabla = args.extxt
    
      print('INGRESE USUARIO DE DB')
      dbuser = input('INGRESE')
      print('INGRESE PASS DE DB')
      dbpass = input('INGRESE')
      print('INGRESE NOMBRE DE DB')
      dbname = input('INGRESE')

      conex = registrarDB(dbuser,dbpass,dbname)

      conex.txt(nomTabla)

    if args.exjson:
       nomTabla = args.exjson
       print('INGRESE USUARIO DE DB')
       dbuser = input('INGRESE')
       print('INGRESE PASS DE DB')
       dbpass = input('INGRESE')
       print('INGRESE NOMBRE DE DB')
       dbname = input('INGRESE')

       conex = registrarDB(dbuser,dbpass,dbname)

       conex.json(nomTabla)
       
    if args.excsv:
       nomTabla = args.excsv
       print('INGRESE USUARIO DE DB')
       dbuser = input('INGRESE')
       print('INGRESE PASS DE DB')
       dbpass = input('INGRESE')
       print('INGRESE NOMBRE DE DB')
       dbname = input('INGRESE')

       conex = registrarDB(dbuser,dbpass,dbname)
       print(nomTabla)
       conex.csv(nomTabla)

if args.subparser_name == 'mys':
    ptrDB = 'mys'
    if args.extxt:
      nomTabla = args.extxt
    
      print('INGRESE USUARIO DE DB')
      dbuser = input('INGRESE')
      print('INGRESE PASS DE DB')
      dbpass = input('INGRESE')
      print('INGRESE NOMBRE DE DB')
      dbname = input('INGRESE')

      conex = registrarDB(dbuser,dbpass,dbname)

      conex.txt(nomTabla)

    if args.exjson:
      nomTabla = args.exjson
      print('INGRESE USUARIO DE DB')
      dbuser = input('INGRESE')
      print('INGRESE PASS DE DB')
      dbpass = input('INGRESE')
      print('INGRESE NOMBRE DE DB')
      dbname = input('INGRESE')

      conex = registrarDB(dbuser,dbpass,dbname)
      print(nomTabla)
      conex.json(nomTabla)

    if args.excsv:
      nomTabla = args.excsv
      print('INGRESE USUARIO DE DB')
      dbuser = input('INGRESE')
      print('INGRESE PASS DE DB')
      dbpass = input('INGRESE')
      print('INGRESE NOMBRE DE DB')
      dbname = input('INGRESE')

      conex = registrarDB(dbuser,dbpass,dbname)
      print(nomTabla)
      conex.csv(nomTabla)

