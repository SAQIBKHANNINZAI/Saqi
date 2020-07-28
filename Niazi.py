#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To SAQIBKHANNINZAI
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

##### LOGO #####
logo = """
\033[1;96m
░██████╗░█████╗░░██████╗░██╗██████╗░
██╔════╝██╔══██╗██╔═══██╗██║██╔══██╗
╚█████╗░███████║██║██╗██║██║██████╦╝
░╚═══██╗██╔══██║╚██████╔╝██║██╔══██╗
██████╔╝██║░░██║░╚═██╔═╝░██║██████╦╝
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░
\033[1;96m
██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
\033[1;96m🇳​​​​​🇮​​​​​🇳​​​​​🇿🇦​​​​​🇮​​​​​
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;47m\033[1;31m      love NIAZI POWER    \033[1;0m
\033[1;96m«-\٠\l ●▬▬▬▬●♥♥♥♥●▬▬­▬▬●
\٠\l ✪✫ ╭╬─☆ SAQI☆─╬╮✫✪
\٠\c ✪✫ ╰╬─☆KAKA☆─╬╯✫✪ \٠\l ●▬▬▬▬●♥♥♥♥●▬▬­▬▬●
----------------\033[1;91mSAQIKAKA\033[1;96m-----------------»
\033[1;91m  ┈┈┈┈┈┈┈  SAQI
\033[1;91m  ┈┈┈┈┈┈┈  SAQIKAKA
\033[1;91m  ┈┈┈┈┈┈┈┈┈┈ 
\033[1;91m  ┈┈┈┈┈┈┈┈   WhatsApp
\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈┈┈-̴̬͖͇̟̟̼̱͙̠͉͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈ 03126707840
\033[1;96m«-----------------\033[1;91mSAQIKAKA\033[1;96m-----------------»"""   
R = '\033[1;91m'
G = '\033[1;92m'                                
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std #SAQI###
def love(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

def menu():
    clear()
    os.system('clear')
    print(logo)
    time.sleep(0.05)
    print("\033[1;41m\033[1;37m1   To return to this menu from any Tool   \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m2\033[1;37m       Stop Process Press CTRL + z        \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m3\033[1;37m         Type python2 Cloning.py          \033[1;0m")
    time.sleep(0.05)
    print( OPERATE WithOut Fb Id        ●")
    time.sleep(0.05)
    print(  OPERATE Facebook login      ●")
    time.sleep(0.05)
    
    print([18] Update  TOOL                     ●")
    time.sleep(0.05)
    print("\033[1;91m[0]  EXIT")
    time.sleep(0.05)
    KAKA()
def KAKA():
	SAQI = raw_input("\033[1;91mSlect option>>>")
	if SAQI =="":
		print ("Select a valid option !")
		KAKA()
	elif SAQI =="1":
		clear()
	        print(
█▄░█ █ █▄░█ ▀█ ▄▀█ █
█░▀█ █ █░▀█ █▄ █▀█ █ )
	        os.system("rm -rf $HOME/402")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/0312")
                print (logo)
	        love(Tool User Name :Saqi ")
                love(Tool Password  :Kaka ")
                time.sleep(5)
                os.system("cd $HOME/402 && python2 Cloningx-2-1.py")
	elif black =="2":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/blackhole")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/blackhole")
                print (logo)
	        love("\033[1;93mTool User Name :\033[1;95m     Saqi ")
                love("\033[1;93mTool Password  :\033[1;95m     Kaka ")
                love("\033[1;93m        :Target Attack  :     ")
                love("\033[1;93mPassword list  :\033[1;95mlovehacker-2.txt ")
                time.sleep(5)
                os.system("cd $HOME/blackhole && python2 AsifJaved.py")
	elif black =="3":
	        clear()
	   
		
 
                
	elif black =="3":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Testing")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Testing")
                print (logo)
	        love("\033[1;93mCongratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/CoviD-19 && python2 Project.py")
	elif black =="0":
	    os.system("exit")
if __name__ == "__main__":
    menu()
