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

- Collect of Genarate Some txt files Containing With Password (For Linux User [read-this](https://www.geeksforgeeks.org/kali-linux-crunch-utility/) to genarate Password Files)

** You Would eed more than one password files,This Brute Force Support Concurrency so due to this it's able try passwords from differnt files same time until it's get the correct password or fineshes all passwords.

- Run The Python code with '-th' argument and write how much workers you want (it't recommend to keep it equal with available threads in your system) and The more workers you will choose the more passwords files you need.

```bash
python Mysql.py -th <numbers of workers>
    or,
python3 Mysql.py -th <numbers of workers>
```
- After Runing The Code it will Create a Folder called 'All_Pass' you need to put all password files there (ex: in my case I chosen 2 threads to I have to put 2 passwords files there and then press enter in the terminal (where the code is running) to continue the process

** That's All If The Correct Password is in any password file it will inform you.
