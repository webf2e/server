from flask import Blueprint,request,abort,Response
from util import FirewallUtil
import json

firewallRoute = Blueprint('firewallRoute', __name__)


@firewallRoute.route('/firewall/status',methods=["POST"])
def status():
    return FirewallUtil.getStatus()


@firewallRoute.route('/firewall/close',methods=["POST"])
def close():
    return FirewallUtil.close()


@firewallRoute.route('/firewall/open',methods=["POST"])
def open():
    return FirewallUtil.start()


@firewallRoute.route('/firewall/portlist',methods=["POST"])
def portlist():
    return Response(json.dumps(FirewallUtil.portlist()), mimetype='application/json')


@firewallRoute.route('/firewall/addport',methods=["POST"])
def addport():
    port = request.form.get("port")
    return FirewallUtil.addport(port)


@firewallRoute.route('/firewall/delport',methods=["POST"])
def delport():
    port = request.form.get("port")
    return FirewallUtil.delport(port)


@firewallRoute.before_request
def print_request_info():
    urlPath = str(request.path)
    if urlPath.find("firewall") != -1:
        agent = str(request.headers.get("User-agent"))
        print("访问admin的agent：{}".format(agent))
        if(agent.find("MI 9 Transparent Edition") == -1):
            #abort(400)
            pass