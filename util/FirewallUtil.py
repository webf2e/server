import os

def getStatus():
    process = os.popen("systemctl status firewalld")
    output = process.read()
    process.close()
    lines = output.split("\n")
    for line in lines:
        line = str(line).strip()
        if "" == line:
            continue
        if line.startswith("Active:"):
            return line.replace("Active:","").strip()

def start():
    process = os.popen("systemctl start firewalld")
    output = process.read()
    process.close()
    return str(output)

def close():
    process = os.popen("systemctl stop firewalld")
    output = process.read()
    process.close()
    return str(output)


def portlist():
    process = os.popen("firewall-cmd --zone=public --list-ports")
    output = process.read()
    process.close()
    return str(output).split()

def addport(port):
    process = os.popen("firewall-cmd --zone=public --add-port={}/tcp --permanent".format(port))
    output = process.read()
    process.close()
    #reload
    process = os.popen("firewall-cmd --reload")
    output = process.read()
    process.close()
    return "success"


def delport(port):
    process = os.popen("firewall-cmd --zone=public --remove-port={}/tcp --permanent".format(port))
    output = process.read()
    process.close()
    #reload
    process = os.popen("firewall-cmd --reload")
    output = process.read()
    process.close()
    return "success"