from git import *
import json,os,shutil,requests,time
from util import SysUtil

gitPath = "/home/liuwenbin/Desktop/git/timetravel"
projectPath = "/home/liuwenbin/Desktop/timetravel"
checkUrl = "http://lovexj.pro/restart/check"

def getGitLog():
    g = Git(gitPath)
    lines = g.log("-1").split("\n")
    result = {}
    for line in lines:
        line = line.strip()
        if "" == line:
            continue
        if line.startswith("Date:"):
            result["date"] = line.replace("Date:", "").strip()
    result["commit"] = lines[-1].strip()
    return result

def gitPull():
    try:
        repo = Repo(gitPath)
        remote = repo.remote()
        remote.pull()
        return "OK"
    except Exception as e:
        return "ERROR"

def moveFiles():
    result = {}
    deployFile = os.path.join(gitPath, "deploy")
    if not os.path.exists(deployFile):
        result["error"] = "{}文件不存在，不能自动部署".format(deployFile)
        return result
    lines = open(deployFile, "r+")
    count = 0
    for line in lines:
        line = line.strip()
        if "" == line:
            continue
        fromName = os.path.join(gitPath, line)
        toName = os.path.join(projectPath, line)
        if os.path.isfile(fromName):
            # 转移文件
            shutil.copy(fromName, toName)
            count += 1
            print("复制文件从{}到{}".format(fromName, toName))
        else:
            # 转移文件夹，只转移文件夹下的文件，不转移子目录
            if not os.path.exists(toName):
                os.mkdir(toName)
            files = os.listdir(fromName)
            for file in files:
                fromFileName = os.path.join(fromName, file)
                if os.path.isfile(fromFileName):
                    toFileName = os.path.join(toName, file)
                    shutil.copy(fromFileName, toFileName)
                    count += 1
                    print("复制文件夹从{}到{}".format(fromFileName, toFileName))
    result["error"] = ""
    result["count"] = count
    return result

def autoDeploy(isRestart):
    result = {}
    result["error"] = ""
    r = gitPull()
    if "OK" == r:
        r = moveFiles()
        if r["error"] == "":
            result["count"] = r["count"]
            if isRestart == "True":
                SysUtil.restart()
                result["isRestart"] = "True"
            else:
                result["isRestart"] = "False"
        else:
            result["error"] = r["error"]
    else:
        result["error"] = "从git上拉取失败"
    try:
        log = getGitLog()
        result["date"] = log["date"]
        result["commit"] = log["commit"]
    except:
        pass
    #调用接口判断是否成功
    for i in range(0,10):
        try:
            r = requests.get(checkUrl)
            if r.text == "OK":
                result["check"] = "服务正常"
                break
            else:
                result["check"] = r.text
        except:
            result["check"] = "服务异常"
        time.sleep(1)
    return result
