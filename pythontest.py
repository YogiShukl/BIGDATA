
import pandas as pd
# import pymssql # connect to sql server
import os
import datetime
import csv
import datetime as dt
import MySQLdb
import mysql.connector
from sqlalchemy import create_engine


from datetime import date
today = date.today()

os.chdir("D:\TID Automation")
os.getcwd()
print("job started at : " + str(datetime.datetime.time(datetime.datetime.now())))
Master = pd.read_excel(r'D:\TID Automation\Input\master.xlsx')
Master = Master[['MENAME','TID','IMPDATE','Status','Final Status']]

Master.rename(columns={'Final Status': 'Final_Status'}, inplace=True)

Master.to_csv('Master.csv',index =False)
