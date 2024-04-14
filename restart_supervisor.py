#!/usr/bin/python
import importlib,sys
importlib.reload(sys)
#sys.setdefaultencoding('utf-8')
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

import os
import time
import string
import subprocess
import threading

progs = {}
threads = []


def prog_restart(func):
        for p in func:
                cmd = '''restart %s''' % p
                logging.info(cmd)
                cmd = '''/home/work/supervisor/bin/supervisorctl pid %s''' % p
                pid = os.popen(cmd).read()
                if int(pid) == 0:
                        cmd = '''is not runing,starting %s''' % p
                        logging.info(cmd)
                        cmd = '''/home/work/supervisor/bin/supervisorctl start %s''' % p
                        out = os.popen(cmd).read()
                        logging.info(out)
                        continue

                cmd = '''kill -9 %s''' % (pid)
                out = os.popen(cmd).read()
                time.sleep(5)
                # check progs is runing!
                cmd = '''/home/work/supervisor/bin/supervisorctl pid %s''' % p
                pid = os.popen(cmd).read()
                if int(pid) == 0:
                        logging.info("start error,exit!")
                        sys.exit(123)
                else:
                        if p.find(':') != -1:
                                cmd = '''/usr/sbin/lsof -p %s|grep LISTEN|wc -l''' % (pid.strip())
                                listen_num = subprocess.check_output([cmd], shell=True)
                                if int(listen_num) == 0:
                                        # retry 1 time
                                        time.sleep(25)
                                        cmd = '/usr/sbin/lsof -p %s|grep LISTEN -c' % (pid.strip())
                                        listen_num = subprocess.check_output(cmd, shell=True)
                                        if int(listen_num) == 0:
                                                if p.find(':') != -1:
                                                        logging.info("bind port error,exit! and retry 1 times!")
                                                        sys.exit(124)
for line in sys.stdin:
        prog_key = line.split(' ')[0].split(':')[0]
        prog = set([line.split(' ')[0]])
        if prog_key in progs:
                progs[prog_key] = progs[prog_key].union(prog)
        else:
                progs[prog_key] = set([])
                progs[prog_key] = progs[prog_key].union(prog)
for k, v in progs.items():
        t1 = threading.Thread(target=prog_restart, args=(v,))
        threads.append(t1)
for t in threads:
        t.setDaemon(True)
        t.start()
for t in threads:
        t.join()
