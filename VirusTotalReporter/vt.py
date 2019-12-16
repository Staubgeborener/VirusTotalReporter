#!/usr/bin/env python3

import report_builder

import sys
import requests
import hashlib
import time

import json
from json2html import *

import os, glob
from os import listdir
from os.path import isfile, join
from colorama import Fore, Back

#-------------------------------
def api_failure(response_code, txt, file):
  if "204" in response_code:
    log = file + ": "  + response_code + " Request rate limit exceeded. You are making more requests than allowed. \
    You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.\n"
  elif "400" in response_code:
    log = file + ": " + response_code + " Bad request. Your request was somehow incorrect. This can be caused by missing arguments or arguments with wrong values.\n"
  elif "403" in response_code:
    log = file + ": " + response_code + " Forbidden. You don't have enough privileges to make the request. \
    You may be doing a request without providing an API key or you may be making a request to a Private API without having the appropriate privileges.\n"
  else:
    log = file + ": Unknown error, please visit https://developers.virustotal.com/reference#api-responses for more informations\n"
  log = log[1:]
  if txt is not "1":
    txt.insert('insert', log)
    txt.see("end")
  else:
    print(Fore.RED + "> Error: " + log[:-1])

#-------------------------------
def create_dir(input_file, input_dir, output, CLI):
  #check parameters - only necessary if GUI is in use, so check CLI variable
  if CLI is "0":
    if (input_file and input_dir):
      log = "Choose only one input (either file or directory)\n"
      return log
    elif not (input_file or input_dir) and not output:
      log = "Choose an input and an output\n"
      return log
    elif not output:
      log = "Choose an output\n"
      return log
    elif not (input_file or input_dir):
      log = "Choose an input\n"
      return log

  #create the report directory for all html-files
  #avoid double slash
  if output.endswith('/'):
    output = output[:-1]

  try:
    os.mkdir(output+"/reports")
  except OSError:
    log = "Creation of the directory %s/reports/ failed, maybe it's already created\n" % output
  else:
    log = "Successfully created the directory %s/reports/\n" % output

  #failure has to be red in CLI version
  if CLI is "1" and "failed" not in log:
    print (log)
  elif CLI is "1":
    print (Fore.RED + "> " + log[:-1])
  elif CLI is not "1":
    return log

def script(api_key, input_file, input_dir, output, txt, delay):
  if input_file:
    file = input_file
  elif input_dir:
    file = input_dir

  #check if parameter is a file or a directory
  isDirectory = os.path.isdir(file)
  if isDirectory:
      #Directory (-> check for / at the end)
      if file.endswith('/'):
          file = file[:-1]
      file = file + "/"
      files = [f for f in listdir(file) if isfile(join(file, f))]
  else:
      files = file

  virustotal_api(api_key, files, output, txt, isDirectory, delay)

#-------------------------------
def virustotal_api(api_key, files, output, txt, dir, delay):
  #use epoch_time for reportname (unambiguously kind of name)
  epoch_time = int(time.time())
  reportname = "/report_" + str(epoch_time) + ".html"

  html = report_builder.header()

  f = open(output + reportname, "w")
  f.write (html)
  f.close()

  if delay: count = len(files)

  for infile in files:
    if delay: count = count - 1
    if dir:
      head_tail = os.path.split(infile)
    else:
      head_tail = os.path.split(files)

    #only filename + encoding before hashing
    infile = str(head_tail[1]).encode('utf-8')
    md5 = hashlib.md5(infile).hexdigest()

    #EICAR-test-file for debugging purpose
    #EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
    #md5 = hashlib.md5(EICAR).hexdigest()

    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': md5}
    response = requests.get(url, params=params)

    if "200" in str(response):
      #create report
      infile = infile.decode('utf-8')
      infile_html = "<table border=\"1\"><tr><th>Name</th><td>" + infile + "</td></tr>"
      result_html = json2html.convert(json = json.dumps(response.json(), sort_keys=True, indent=4))
      result_html = result_html[18:] #cut off old table header

      f = open(output+"/reports/" + infile + ".html", "w")
      f.write ('{0} {1}\n'.format(infile_html, result_html))
      f.close()

      data = json.loads(json.dumps(response.json(), sort_keys=False, indent=4))
      #avoid key error problems, if there is no 'positives' or 'total' section in json
      check = ['positives', 'total']
      if not any(x in data for x in check):
        data_positives = data_total = "0"
      else:
        data_positives = str(data['positives'])
        data_total = str(data['total'])

      #add threshold-colors in report
      try:
        calc = int(data_positives) / int(data_total)
      except ZeroDivisionError:
        calc = 0.0

      if(calc < 0.1):
        color = "green"
      elif(calc < 0.33):
        color = "orange"
      else:
        color = "red"

      html = "<a href=./reports/" + infile + ".html target=\"myFrame\"><font color=\"" + color + "\">" + infile + " - " + data_positives + "/" + data_total + "</font></a>"

      f = open(output + reportname, "a")
      f.write (html + '\n')
      f.close()

      log = "Created " + infile + ".html in reports folder\n"
      if txt is not "1":
        txt.insert('insert', log)
        txt.see("end")
      else:
        print("> " + log[:-1])
      if not dir: break

    else:
      api_failure(str(response), txt, str(infile))

    #hack: 4 requests per minute = 15 seconds delay, so you can check a lot of files without getting errors
    #only delaying, if there is no inquiry left (count > 0; count is number of elements in 'files')
    if delay and count > 0: 
      log = "Delay: Waiting 15 seconds ...\n" #program may not respond, keep calm
      if txt is not "1":
        txt.insert('insert', log)
        txt.see("end")
        txt.update() #use update(), otherwise sleep is not working
      else:
        print("> " + log[:-1])
      time.sleep(15)

  end(output, txt, reportname)

#-------------------------------
def end(output, txt, reportname):
  #footer
  html = report_builder.footer()
  f = open(output + reportname, "a")
  f.write (html)
  f.close()

  log = "Created " + reportname[1:] + " successfully\n"
  if txt is not "1":
    txt.insert('insert', log)
    txt.see("end")
  else:
    print(Fore.GREEN + "> " + log)

#-------------------------------
if __name__ == "__main__":
    main()
