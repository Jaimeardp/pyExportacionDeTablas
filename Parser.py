import argparse
from conmysql import *

global nomTabla


class ViewTableWithFormat(object):
	"""docstring for ViewTableWithFormat"""
	def __init__(self, arg):
		super(ViewTableWithFormat, self).__init__()
		self.arg = arg
		







###### MAIN ######

parser = argparse.ArgumentParser(description='Mi Primer Hola Mundo')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('-s','--sum', dest='accumulate', action='store_const',const = sum, default= max , help='sum the integers (default: find the max)')
parser.add_argument("-js","--exjson", help="Ingrese tabla para exportar en formato json \n > e.g tbl_name")
parser.add_argument("-txt","--extxt", help="Ingrese tabla para exportar en formato txt \n > e.g tbl_name")
args = parser.parse_args()

print('WHAT SAID ',args.json)
print(type(args.json))

if args.exjson:
	nomTabla = args.exjson
if args.extxt:
	nomTabla = args.extxt

#if args.target:
#	print('PRUEBA')
    #target = args.target
    #showDisplay(displayMode,BLUE+"[SET] target => "+args.target+END)
    #targetIP = socket.gethostbyname(target)
    #showDisplay(displayMode,BLUE+"[SET] IP Address => "+targetIP+END)
#if args.sum :
#	print('ENTRO')

#print (args.accumulate(args.integers))