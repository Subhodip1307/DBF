# DBF (Database Brute Force)

## Disclaimer

This repository (DBF) is intended for educational purposes only. The materials and code provided here are for learning and research purposes and should not be used for any illegal activities. 

By accessing, downloading, or using any content from this repository, you agree that:

- You will not engage in any illegal activities using the information or code provided here.
- You are solely responsible for any actions you take based on the content of this repository.
- The maintainers and contributors of this repository are not liable for any misuse or illegal activities conducted using the information or code provided here.

Any use of the content in this repository for illegal purposes is strictly prohibited and may result in legal consequences.

If you have any questions or concerns regarding the contents of this repository, please contact the maintainers.

## Features
  - Easy To Use
  - Flexible
  - Fast & Efficient
  - Support Concurrency

## Requirements
  - Python 3.9.2 or upper
  - Database Host
  - Database User
  - Database Port
  - Passowrd Files

** IF you have linux and want to genarate Passowrd files [read-this](https://www.geeksforgeeks.org/kali-linux-crunch-utility/)

## Supported Database
- MySQL
- PostgreSQL
- (coming Soon.....)

## Get Started

Now we will see how can we brute force a database with the help of this repo (If You Don't Have Permission then you can try it on your own database of your local system)
Follow the step by step guidance to achive your goal.

- Copy the repo to your local machine

```bash

git clone https://github.com/Subhodip1307/DBF.git
```

- Create a Virtual env for python (optional)

Windows

```bash
pip install virtualenv
virtualenv dbenv
dbenv\Scripts\activate 
```
Linux

```
sudo pip3 install virtualenv
python3 -m venv dbenv
source dbenv/bin/activate
```
- Installing all requirements

```bash
pip install -r requirements.txt
            or,
pip3 install -r requirements.txt
```

- Collect or Generate Some txt files Containing With Password (For Linux Users [read-this](https://www.geeksforgeeks.org/kali-linux-crunch-utility/) to generate Password Files)

** You Would need more than one password file, This Brute Force supports concurrency so due to this it's able to try passwords from different files same time until it get the correct password or fineshes all passwords.

- Run The Python code with '-th' argument and write how much workers you want (it's recommended to keep it equal with available threads in your system) and The more workers you will choose the more password files you need. Then Use '-db' and enter the database name , currently its support only two (mysql,postgres). And Finaly Press Enter To start.

syntax:

```bash
python main.py -th <numbers of workers> -db <database type>
    or,
python3 main.py -th <numbers of workers> -db <database type>
```
example:

```bash
python main.py -th 2 -db postgres
    or,
python3 main.py -th 2 -db postgres
```

- After Runing The Code it will Create a Folder called 'All_Pass' you need to put all password files there (ex: in my case I chosen 2 threads to I have to put 2 passwords files there and then press enter in the terminal (where the code is running) to continue the process

** That's All If The Correct Password is in any password file it will inform you.
