import os

projectPath = "/root/python_proj/timetravel"

def getPid():
    output = os.popen('ps -ef | grep uwsgiconfig.ini')
    lines = output.read().split("\n")
    pid = None
    for line in lines:
        ls = line.split()
        if len(ls) < 3:
            continue
        if ls[2] == "1":
            pid = ls[1]
            break
    return pid

def kill(pid):
    # 返回0，成功，其他失败
    if isStarted():
        return os.system("kill -9 {}".format(pid))
    return "NOT_STARTED"

def start():
    if not isStarted():
        return os.system("sh {}/run.sh".format(projectPath))
    return "ALREADY_STARTED"

def restart():
    shell = "sh {}/restart.sh {} &".format(projectPath, getPid())
    print(shell)
    return os.system(shell)

def isStarted():
    if getPid() == None:
        return False
    return True

#webssh

def getWebsshPid():
    output = os.popen('netstat -ntlp | grep 8800')
    lines = output.read().split("\n")
    pid = None
    for line in lines:
        ls = line.split()
        if len(ls) == 0:
            continue
        pid = ls[-1].split("/")[0]
    return pid

def killWebssh(pid):
    # 返回0，成功，其他失败
    if isWebsshStarted():
        return os.system("kill -9 {}".format(pid))
    return "NOT_STARTED"

def startWebssh():
    if not isWebsshStarted():
        return os.system("sh {}/shell/webssh.sh".format(projectPath))
    return "ALREADY_STARTED"

def restartWebssh():
    shell = "sh {}/shell/restartWebssh.sh {} &".format(projectPath, getWebsshPid())
    print(shell)
    return os.system(shell)

def isWebsshStarted():
    if getWebsshPid() == None:
        return False
    return True