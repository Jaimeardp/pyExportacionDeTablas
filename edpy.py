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
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('-s','--sum', dest='accumulate', action='store_const',const = sum, default= max , help='sum the integers (default: find the max)')
subparsers = parser.add_subparsers(help='sub-command help',dest='subparser_name')

parse_orc = subparsers.add_parser('orc')
parse_orc.add_argument('-js',"--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_orc.add_argument('-txt',"--extxt", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")

parse_mys = subparsers.add_parser('mys')
parse_mys.add_argument('-js',"--exjson",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parse_mys.add_argument('-txt',"--extxt",help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
#"--exjson", |  "--extxt", 
'''
parser.add_argument('-orc','--oracle', action='store_true', help='Oracle Info')
parser.add_argument('-mys','--mysql', action='store_true', help='MySQL Info')
subparsers1 = parser.add_subparsers(help='sub-command help')

#parser_a = subparsers.add_parser('a', help='a help')
#parser_a.add_argument('bar', type=int, help='bar help')
parser_a = subparsers.add_parser()
parser_a.add_argument('js',"--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
#parser_b = subparsers.add_parser('txt', help='b help')
parser_a.add_argument('txt',"--extxt", help="Ingrese tabla para exportar en formato txt \n > e.g tbl_name")
#parser_b = subparsers.add_parser('b', help='b help')
#parser_b.add_argument('--baz', choices='XYZ', help='baz help')


parser_a1 = subparsers1.add_parser()
parser_a1.add_argument('js',"--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
#parser_b1 = subparsers1.add_parser('txt', help='b help')
parser_a1.add_argument('txt',"--extxt", help="Ingrese tabla para exportar en formato txt \n > e.g tbl_name")

#parser.add_argument("-js","--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
#parser.add_argument("-txt","--extxt", help="Ingrese tabla para exportar en formato txt \n > e.g tbl_name")'''
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

#if args.target:
#   print('PRUEBA')
#    #target = args.target
#    #showDisplay(displayMode,BLUE+"[SET] target => "+args.target+END)
#   #targetIP = socket.gethostbyname(target)
#    #showDisplay(displayMode,BLUE+"[SET] IP Address => "+targetIP+END)
#if args.sum :
#   print('ENTRO')

#print (args.accumulate(args.integers))