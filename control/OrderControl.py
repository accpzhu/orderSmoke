import ConfigParser
import os
from model import User
from service import LoginService

class OrderControl(object):
    def __init__(self):
        self.loginService=LoginService.LoginService()

    def doOrder(self):
        cp = ConfigParser.SafeConfigParser()
        cp.read(os.path.abspath('.') + '\\resource\\resource.ini')
        user=User.User(cp.get('users', 'username'),cp.get('users', 'password'))
        self.loginService.login(user,cp.get('url', 'url'),os.path.abspath('.') + '\\resource\\'+cp.get('driver', 'driverName'))