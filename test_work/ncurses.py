#!/usr/bin/env python2

from os import system
import curses
import json


with open('../stations.json') as json_data:
     stations = json.load(json_data)
     json_data.close()

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""
x = 0



while x != ord('q'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "Radio Player. q to quit")
    screen.addstr(2, 2, "Station List")
    station_tuple = tuple(stations)
    i = 0
    for station_index in station_tuple:
         screen.addstr(i+3, 2,  str(station_tuple.index(station_index)) + ": " + station_index)
         i += 1
    #screen.addstr(3, 2, str(len ( stations.keys() )))
    #screen.addstr(4, 4, " user")
    #screen.addstr(5, 4, "2 - Restart Apache")
    #screen.addstr(6, 4, "3 - Show disk space")
    #screen.addstr(i+3, 2, str(i) + str(x))


    #screen.addstr(i+5, 2, str(x))
    try:
        val = int(chr(x))
        screen.addstr(i+4, 2, "Will try to play " + str((chr(x))))
        screen.addstr(i+5, 2, str(val))
    except ValueError:
        print("That's not an int!")

    if x is ord("s"):
         screen.addstr(i+6, 2, "Shtop!")
    screen.refresh()
    #if x == ord('1'):
    #    print "Test"
    #    username = get_param("Enter the username")
    #    homedir = get_param("Enter the home directory, eg /home/nate")
    #    groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
    #    shell = get_param("Enter the shell, eg /bin/bash:")
    #    curses.endwin()
    #    execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
    #if x == ord('2'):
    #    curses.endwin()
    #    execute_cmd("apachectl restart")
    #if x == ord('3'):
    #    curses.endwin()
    #    execute_cmd("df -h")
    x = screen.getch()
curses.endwin()
