import pymysql
from pandas import DataFrame, Series
import pandas as pd
import numpy

class Connection(object):
    """docstring for Connection"""

    dbusername = ''
    dbpassword = ''
    dbname = ''

    def __init__(self, dbusername,dbpassword,dbname):
        super(Connection, self).__init__()
        self.dbusername = dbusername
        self.dbpassword = dbpassword
        self.dbname = dbname

    def _Con(self):
        db = pymysql.connect(user = self.dbusername, passwd = self.dbpassword, db = self.dbname)
        return db

    def mostrar_tbl(self ,nom):
        db = self._Con()
        cursor = db.cursor()
        query = 'select * from '+nom
        cursor.execute(query)
        # retrieve the result 
        results = cursor.fetchall()
        for li in results: 
          print(li,'\n')

    def txt(self,nom):
        dic = dict()
        db = self._Con()
        cursor =  db.cursor()
        query = 'select * from '+nom
        cursor.execute(query)
        results = cursor.fetchall()
        print(type(results))
        #print(results)
        l = list(results)
        frame = DataFrame(l)
        #print(frame[:10])
        arr = open('nuevo.txt','w')
        for l in range(0,len(frame)):
            dic[l] = []
            for i in frame:
                dic[l].append(frame[i][l])
                arr.write(str(frame[i][l])+',')
            arr.write('\n')

        return dic

    def json(self,nom):
        pass

                  
#?INDICES DEL FRAME NO UTILIZADO



con = Connection('root','mysql','prestocash')

#con.mostrar_tbl('tb_cliente')

di= con.txt('tb_cambio')

print(di)




 

 

