import locale,os,subprocess,shlex
def execute(cmd):
    cmd = cmd.striip()
    if not cmd:
        return ""
    
    if os.name == "nt":
        shell=True
    else:
        shell=False
    
    #outputを作る
    output= subprocess.check_output(
        shlex.split(cmd),
        stderr=subprocess.STDOUT,
        shell=shell
    )
    
    if locale.getdefaultlocale() == ('jp_JP','cp932'):
        return output.decode('cp932',errors='ignore')
    else:
        return output.decode(errors='ignore')