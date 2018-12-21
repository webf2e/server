from flask import Blueprint
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