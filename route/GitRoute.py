from flask import Blueprint,request,abort,Request,Response
from util import SysUtil,GitUtil
import json

gitRoute = Blueprint('gitRoute', __name__)

@gitRoute.route('/git/log',methods=["POST"])
def gitLog():
    return Response(json.dumps(GitUtil.getGitLog()), mimetype='application/json')

@gitRoute.route('/git/pull',methods=["POST"])
def gitPull():
    return GitUtil.gitPull()

@gitRoute.route('/git/moveFiles',methods=["POST"])
def moveFiles():
    return Response(json.dumps(GitUtil.moveFiles()), mimetype='application/json')

@gitRoute.route('/git/autoDeploy',methods=["POST"])
def autoDeploy():
    isRestart = request.form.get("isRestart")
    return Response(json.dumps(GitUtil.autoDeploy(isRestart)), mimetype='application/json')

@gitRoute.before_request
def print_request_info():
    urlPath = str(request.path)
    if urlPath.find("git") != -1:
        agent = str(request.headers.get("User-agent"))
        print("访问admin的agent：{}".format(agent))
        if(agent.find("MI 9 Transparent Edition") == -1):
            #abort(400)
            pass