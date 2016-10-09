#!/usr/bin/env python
import os, pwd

def show_message(mess):
    print mess

def for_loop_example():
    for num in range(1,11):
        print num

def foreach_example():
    fruits = ['ram','cpu','motherboards']
    for fruit in fruits:
        print fruit

def get_system_info():
    #os.getlogin doesn't work as we expect within docker
    #see http://stackoverflow.com/questions/4399617/python-os-getlogin-problem
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]

    print 'CURRENT USER: ', os.getlogin()
    print 'HOME DIR: ', os.path.expanduser('~')

def run_system_commands():
    print 'SHOW DIR: ', os.getcwd()
    os.system('ls -alt')

def main():
    #show_message("hello world")
    #for_loop_example()
    #foreach_example()
    get_system_info()
    run_system_commands()

if __name__ == "__main__":
    main()
