import cx_Oracle 
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json
class ConnectionOracle(object):
    """docstring for Connection"""

    dbusername = ''
    dbpassword = ''
    dbname = ''

    def __init__(self, dbusername,dbpassword,dbname):
        super(ConnectionOracle, self).__init__()
        self.dbusername = dbusername
        self.dbpassword = dbpassword
        self.dbname = dbname

    def _Con(self):
        cad = self.dbusername+'/'+self.dbpassword+'@127.0.0.1:1521/'
        db = cx_Oracle.connect(cad+self.dbname)
        return db

    def mostrar_tbl(self ,nom):
        db = self._Con()
        cursor = db.cursor()
        query = 'select * from '+nom
        cursor.execute(query)
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
        listac = list()
        db = self._Con()
        cursor =  db.cursor()
        query = 'select * from '+nom
        #---------------------------------
        cursor.execute("select column_name from all_tab_columns where table_name= '"+ nom +"' ")
        cols = cursor.fetchall()
        l1 = list(cols)
        arr = np.array(l1)
        arr = arr[0:len(l1),:1]
        arr.shape = (len(l1),)
        #----------------------------------
        cursor.execute(query)
        results = cursor.fetchall()
        #print(type(results))
        l = list(results)
        frame = DataFrame(l,columns=arr)
        js = frame.to_json(orient="records")
        #print(type(js))
        #print(js)
        data = json.loads(js)
        with open('nuevo1.json','w') as outfile:
            json.dump(data,outfile)
        return js

    def csv(self):
        pass           


#?INDICES DEL FRAME NO UTILIZADO



 

 

