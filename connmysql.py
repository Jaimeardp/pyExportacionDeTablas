import pymysql
from pandas import DataFrame, Series
import pandas as pd
import numpy
import json
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
        l = list(results)
        frame = DataFrame(l)
        arr = open('nuevo.txt','w')
        for l in range(0,len(frame)):
            dic[l] = []
            for i in frame:
                dic[l].append(frame[i][l])
                arr.write(str(frame[i][l])+',')
            arr.write('\n')

        return dic


    def json(self,nom):
        db = self._Con()
        cursor =  db.cursor()
        query = 'select * from '+nom
        cursor.execute(query)
        results = cursor.fetchall()
        print(type(results))
        l = list(results)
        frame = DataFrame(l)
        js = frame.to_json(orient="records")
        print(type(js))
        print(js)
        data = json.loads(js)
        with open('nuevo1.json','w') as outfile:
            json.dump(data,outfile)

        return js

                  
#?INDICES DEL FRAME NO UTILIZADO



con = Connection('root','mysql','prestocash')

con.mostrar_tbl('tb_estado_articulo')

#di= con.txt('tb_cambio')

#print(di)

js = con.json('tb_estado_articulo')
print(js)



 

 

