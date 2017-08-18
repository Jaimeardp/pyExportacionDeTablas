import os
import sys
sys.path.append(os.path.dirname( os.path.abspath( __file__ ))+"/module")
import argparse
from connmysql import *

global nomTabla

######### VIEW SHELL ###########################

class ViewTableWithFormat(object):
	"""docstring for ViewTableWithFormat"""
	def __init__(self, arg):
		super(ViewTableWithFormat, self).__init__()
		self.arg = arg
	
	def __call__(self):
		pass


############## CONEXIONES A LAS DB'S ###############	
def registrarDB(dbuser,dbpass,dbname):
	CON = Connection(dbuser,dbpass,dbname)
	return CON


######################## MAIN #######################
parser = argparse.ArgumentParser(description='Mi Primer Hola Mundo')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('-s','--sum', dest='accumulate', action='store_const',const = sum, default= max , help='sum the integers (default: find the max)')
parser.add_argument("-js","--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parser.add_argument("-txt","--extxt", help="Ingrese tabla para exportar en formato txt \n > e.g tbl_name")
args = parser.parse_args()

#print('WHAT SAID ',args.json)
#print(type(args.json))

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

#if args.target:
#	print('PRUEBA')
    #target = args.target
    #showDisplay(displayMode,BLUE+"[SET] target => "+args.target+END)
    #targetIP = socket.gethostbyname(target)
    #showDisplay(displayMode,BLUE+"[SET] IP Address => "+targetIP+END)
#if args.sum :
#	print('ENTRO')

#print (args.accumulate(args.integers))