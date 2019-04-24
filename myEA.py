#!/usr/bin/env python
# coding: utf-8
from pandas import DataFrame as df

import pandas as pd

import numpy as np

from sklearn.linear_model import LogisticRegression as LR

from sqlalchemy.types import NVARCHAR, Float, Integer

from sqlalchemy import create_engine

import sqlalchemy

myserver="localhost"

myuser="nina"


mypassword="1234"

mydb="iot"

data=pd.read_csv("training.csv")

X=data['value'].values.reshape(-1,1)


Y=data['status'].values.reshape(-1,1)



print(X.shape,type(X))



modle=LR()



modle.fit(X,Y)
my_score=modle.score(X,Y)
print(my_score)

import pymysql.cursors

conn = pymysql.connect(host=myserver, user=myuser, passwd=mypassword, db=mydb)

c = conn.cursor()

input("ok")

c.execute("SELECT * FROM light")

results = c.fetchall()

print(type(results))

test_df = df(list(results), columns=['id','value','time','status'])

testX=test_df['value'].values.reshape(-1,1)


testY=modle.predict(testX)


test_df['status']=testY

c.execute('update light set status = 0 where value>0')

id_list=list(test_df[test_df['status']==1].id)

for _id in id_list:
    c.execute('update light set status=1 where id='+str(_id))


conn.commit()

c.close()
conn.close()