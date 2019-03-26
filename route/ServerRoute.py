from flask import Blueprint,request,abort
from util import SysUtil

serverRoute = Blueprint('serverRoute', __name__)


@serverRoute.route('/server/startServer',methods=["POST"])
def startServer():
    return str(SysUtil.start())


@serverRoute.route('/server/stopServer',methods=["POST"])
def stopServer():
    return str(SysUtil.kill(SysUtil.getPid()))


@serverRoute.route('/server/restartServer',methods=["POST"])
def restartServer():
    return str(SysUtil.restart())


@serverRoute.route('/server/getPid',methods=["POST"])
def getPid():
    return str(SysUtil.getPid())


@serverRoute.route('/server/isStarted',methods=["POST"])
def isStarted():
    return str(SysUtil.isStarted())


@serverRoute.route('/webssh/start',methods=["POST"])
def startWebssh():
    return str(SysUtil.startWebssh())


@serverRoute.route('/webssh/stop',methods=["POST"])
def stopWebssh():
    return str(SysUtil.killWebssh(SysUtil.getWebsshPid()))


@serverRoute.route('/webssh/restart',methods=["POST"])
def restartWebssh():
    return str(SysUtil.restartWebssh())


@serverRoute.route('/webssh/getPid',methods=["POST"])
def getWebsshPid():
    return str(SysUtil.getWebsshPid())


@serverRoute.route('/webssh/isStarted',methods=["POST"])
def isWebsshStarted():
    return str(SysUtil.isWebsshStarted())


@serverRoute.before_request
def print_request_info():
    urlPath = str(request.path)
    if urlPath.find("server") != -1 or urlPath.find("webssh") != -1:
        agent = str(request.headers.get("User-agent"))
        print("访问admin的agent：{}".format(agent))
        if(agent.find("MI 9 Transparent Edition") == -1):
            abort(400)