import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'
sys.dont_write_bytecode = True

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'ab1.mysql.database.azure.com')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'maria')           
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '42ohosisSD')    
    MYSQL_DB = os.environ.get('MYSQL_DB', 'lab_db')             
