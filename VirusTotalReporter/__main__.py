#!/usr/bin/env python3

import argparse
import webbrowser
import getopt
from pathlib import Path

import vt, information

import tkinter
import tkinter.scrolledtext as scrolledtext
from tkinter import *
from tkinter import filedialog

import os
from os.path import isfile, join

from colorama import Fore, Back, init

#-------------------------------
def center_window(windowWidth, windowHeight, master):
  positionRight = int(master.winfo_screenwidth()/2 - int(windowWidth)/2)
  positionDown = int(master.winfo_screenheight()/2 - int(windowHeight)/2)
  return positionRight, positionDown


#-------------------------------
def clicked_new_api_key(api, window, txt):
  f = open('.virustotal_api_key', 'w')
  f.write(api)
  f.close()

  txt.insert('insert', "Successfully set a new API key\n")
  txt.see("end")

  window.destroy()

#-------------------------------
def clicked_new_api_key_abort(window, txt):
  txt.insert('insert', "Input of new API key canceled by user\n")
  txt.see("end")

  window.destroy()

#-------------------------------
def clicked_help_1():
  webbrowser.open("https://github.com/Staubgeborener/VirusTotalReporter",0)

#-------------------------------
def clicked_help_2():
  webbrowser.open("https://github.com/Staubgeborener/VirusTotalReporter/issues",0)

#-------------------------------
def clicked_about(master):
  window = tkinter.Toplevel(master)
  display = Label(window, text=information.about())

  #center window
  positionRight, positionDown = center_window("750", "250", window)
  window.geometry("%dx%d+%d+%d" % (750, 250, positionRight, positionDown))
  display.pack()

#-------------------------------
def clicked_input_file(e1):
  filename = filedialog.askopenfilename()
  e1.delete(0, tkinter.END)
  e1.insert(0,filename)

#-------------------------------
def clicked_input_dir(e2):
  filename = filedialog.askdirectory()
  e2.delete(0, tkinter.END)
  e2.insert(0,filename)

#-------------------------------
def clicked_output(e3):
  filename = filedialog.askdirectory()
  e3.delete(0, tkinter.END)
  e3.insert(0,filename)

#-------------------------------
def clicked_save(e4, master, txt):
  window = tkinter.Toplevel(master)
  #center window
  positionRight, positionDown = center_window("170", "100", window)
  window.geometry("%dx%d+%d+%d" % (170, 100, positionRight, positionDown))
  if not e4.get():
    display = Label(window, text="API key is empty").grid(column=1, row=1)
    btnno = Button(window, text="Ok", command=window.destroy).grid(column=1, row=3)
  else: 
    display = Label(window, text="Truly create a new key?").grid(column=1, row=1)
    #var = master.IntVar()
    btnyes = tkinter.Button(window, text="Yes", command=lambda:clicked_new_api_key(e4.get(), window, txt)).grid(column=1, row=2)
    btnno = Button(window, text="No", command=lambda:clicked_new_api_key_abort(window, txt)).grid(column=1, row=3)

#-------------------------------
def clicked_start(api_key, input_file, input_dir, output, txt, delay):
  if not api_key:
    txt.insert('insert', "No API key\n")
    txt.see("end")
  else:
    log = vt.create_dir(input_file, input_dir, output, "0")
    txt.insert('insert', log)
    txt.see("end")
    #check error messages, if everythings alright (aka no input or output messages in log): call api
    check = ['input', 'output']
    if not any(x in log for x in check):
      vt.script(api_key, input_file, input_dir, output, txt, delay)

      #vt.end(output, txt)

#-------------------------------
def gui():
  #check for hidden keyfile, otherweise create an empty one
  keyfile = Path("./.virustotal_api_key")
  if not keyfile.is_file():
    open('.virustotal_api_key', 'a')

  #read keyfile
  with open('.virustotal_api_key', 'r') as keyfile:
    api_key = keyfile.read().rstrip("\n")
  #main window
  master = Tk()
  master.wm_title("VirusTotalReporter")

  #menu
  menu = Menu(master)
  master.config(menu=menu)
  helpmenu = Menu(menu)
  menu.add_cascade(label="Menu", menu=helpmenu)
  helpmenu.add_command(label="Documentation", command=lambda:clicked_help_1())
  helpmenu.add_command(label="Trouble?", command=lambda:clicked_help_2())
  helpmenu.add_command(label="About...", command=lambda:clicked_about(master))
  helpmenu.add_separator()
  helpmenu.add_command(label="Exit", command=master.quit)

  #create text
  lbl1 = Label(master, text='Select File (Input):').grid(row=0)
  lbl2 = Label(master, text='Select Dir (Input):').grid(row=1)
  lbl3 = Label(master, text='Output:', pady=5).grid(row=2)
  lbl4 = Label(master, text='API KEY:', pady=5).grid(row=3)

  #create entries
  e1 = Entry(master, width=50)
  e1.grid(row=0, column=1)
  e2 = Entry(master, width=50)
  e2.grid(row=1, column=1)
  e3 = Entry(master, width=50)
  e3.grid(row=2, column=1)
  e4 = Entry(master, width=65, justify='center')
  e4.grid(row=3, column=1)
  e4.insert(0,api_key)
  delay = tkinter.BooleanVar() 
  Checkbutton(master, text="Delay", variable=delay).grid(row=4, column=3)


  #log
  txt = scrolledtext.ScrolledText(master, wrap=WORD, undo=True, width=100, height=5)
  txt.insert('insert', "")
  txt['font'] = ('consolas', '10')
  txt.grid(row=4, column=1)

  #create button
  btn1 = Button(master, text="Browse", command=lambda:clicked_input_file(e1))
  btn1.grid(column=3, row=0)
  btn2 = Button(master, text="Browse", command=lambda:clicked_input_dir(e2))
  btn2.grid(column=3, row=1)
  btn3 = Button(master, text="Browse", command=lambda:clicked_output(e3))
  btn3.grid(column=3, row=2)
  btn4 = Button(master, text="Save", command=lambda:clicked_save(e4, master, txt))
  btn4.grid(column=3, row=3)
  btn5 = Button(master, text="Start", padx=30, pady=10, command=lambda:clicked_start(e4.get(), e1.get(), e2.get(), e3.get(), txt, delay.get()))
  btn5.grid(column=1, row=5)

  #center window
  positionRight, positionDown = center_window("1025", "275", master)
  master.geometry("%dx%d+%d+%d" % (1025, 275, positionRight, positionDown))

  master.mainloop()

#-------------------------------
def main():
    init(autoreset=True)

    information.gui_header()

    parser = argparse.ArgumentParser("VirusTotalReporter", epilog='Example of use: python VirusTotalReporter -a apikey -o ./output -i ./testfile.virus')
    parser.add_argument('-a', '--apikey', action='store', dest='apikey', help="API key string")
    parser.add_argument('-o', '--output', action='store', dest='output', help="Name of output folder")
    parser.add_argument('-i', '--input', action='store', dest='input', help="Name of input file OR input folder")
    parser.add_argument('-d', '--delay', action='store_true', dest='delay', help="Activate 15 seconds delay between every examination")
    parser.add_argument('-g', '--gui', action='store_true', dest='gui', help="Start GUI")

    #windows starts gui, anything else needs parameter like -g (gui)
    if len(sys.argv)==1:
      if os.name == 'nt':
        gui()
      else:
        parser.print_help(sys.stderr)
        print(Fore.RED + "\nNo parameters passed")
        sys.exit(1)

    args = parser.parse_args()

    #check for apikey, output, input but NO gui 
    if args.apikey and args.output and args.input and not args.gui:
      #no input, just output and CLI = 1
      vt.create_dir("", "", args.output, "1")
      #check delay -d
      if args.delay:
        delay = True
      else:
        delay = False
      #call script with apikey, input/s, output, set CLI = 1, delay
      vt.script(args.apikey, args.input, args.input, args.output, "1", delay)
    #forbid the call of gui AND CLI version
    elif args.apikey and args.output and args.input and args.gui:
      print(Fore.RED + "Either GUI or CLI, not both")
    elif args.gui :
      print("Starting GUI ...")
      gui()

#-------------------------------
if __name__ == '__main__':
    main()
