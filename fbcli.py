#!/usr/bin/python

import sys
import os
from subprocess import check_output,Popen, PIPE, STDOUT
import re

if not len(sys.argv[1:]):
   print '\nUsage: fbcli module\n'
   exit(1)

fbpath = '/root/.wine/drive_c/nsa/windows'

command = sys.argv[1]
args = ' '.join(sys.argv[2:])
#if not args: args = '--help'

modules = [os.path.join(dp, f) for dp, dn, filenames in os.walk(fbpath) for f in filenames if os.path.splitext(f)[1] == '.exe']
if command == 'list':
   for i in modules:
      print i
   exit(0)

commandlist = [i for i in modules if command in i.lower() and not 'legacy' in i.lower()]
if len(commandlist) > 1:
  print '\nThere is more than one instance of %s:' % command
  cnt = 0
  for cmd in commandlist:
    print '[%d] %s' % (cnt,cmd)
    cnt += 1
  ans = raw_input('\nSelect your module: ')
  if not re.match('[0-9]',ans):
    print 'Invalid choice. Exit.'
    exit(1)
  else:
    command = commandlist[int(ans)]
else:
  command = commandlist[0]

module = os.path.basename(command)
path = os.path.dirname(command)

inconfig = [i for i in os.listdir(path) if '.'.join(module.split('.')[:-1]) in i and 'xml' in i][0]

cmd = 'cd %s; TZ=Europe/Berlin wine %s --inconfig %s --OutConfig z:\\\\dev\\\\null %s 2>/dev/null' % (path, module, inconfig, args)

p = Popen(cmd, stdout=PIPE, shell=True)
for line in iter(p.stdout.readline, b''):
   sys.stdout.write(line)
   sys.stdout.flush()
#print check_output(cmd,shell=True)

