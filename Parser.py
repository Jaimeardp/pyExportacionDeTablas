import argparse

parser = argparse.ArgumentParser(description='Mi Primer Hola Mundo')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('-s','--sum', dest='accumulate', action='store_const',const = sum, default= max , help='sum the integers (default: find the max)')
parser.add_argument("-js","--json", help="Target URL and IP Address\n  > e.g -t 127.0.0.1")

args = parser.parse_args()

print('WHAT SAID ',args.json)
print(type(args.json))

#if args.target:
#	print('PRUEBA')
    #target = args.target
    #showDisplay(displayMode,BLUE+"[SET] target => "+args.target+END)
    #targetIP = socket.gethostbyname(target)
    #showDisplay(displayMode,BLUE+"[SET] IP Address => "+targetIP+END)
#if args.sum :
#	print('ENTRO')

#print (args.accumulate(args.integers))