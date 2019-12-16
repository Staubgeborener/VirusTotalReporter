#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

def gui_header():
    print("\n------------------------------------------------------------------ ")
    print(Style.BRIGHT + "               VirusTotal Reporter", end='')
    print(gui_build_ascii()) 
    print("                      Eric Schröder (c)2019")
    print(Fore.YELLOW + "                      staubgeborener@github")
    print(gui_explanation())
    print("------------------------------------------------------------------\n ")


def gui_build_ascii():
    return """    ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅)"""

def gui_explanation():
	return """
       Check files or content of folders with the help of the
  VirusTotal databases (API) and creates a html report at the end
                     for fast malware analyse    

        >> Can be used with GUI or CLI with parameters <<
	"""

def about():
	return "\nVirusTotal Reporter\n\nThis program checks files or content of folders with the\n \
    help of the VirusTotal databases (API) and creates a html report at the end\n for fast malware analyse.\n\n \
    Can be used with GUI or CLI - works with Linux, Mac and Windows.\n\nEric Schröder (c)2019\nstaubgeborener@github"