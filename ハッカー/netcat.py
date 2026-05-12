import argparse
import locale
import os
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return 
    
    if os.name == "nt":
        shell= True
    else:
        shell =False
    output =subprocess.check_output(shell.split(cmd),
                                stderr=subprocess.STDOUT,
                                shell=shell())
    if locale.getdefaultlocale() == ('jp_JP','cp932'):
        return output.decode('cp932')
    else:
        return output.decode()
    
