from connection import r
import string
import random

class Application(object):
    def __init__(self):
        self.conn = r

    def searchForRole(self):
        clientsList=r.client_list()
        clientsRole=[d['name'] for d in clientsList if 'name' in d]
        if (clientsRole.count("generator")>1 and self.conn.client_getname() == 'generator'):
            self.conn.client_setname('handler')
        if ('generator' in clientsRole):
            if(self.conn.client_getname() != 'generator'):
                self.conn.client_setname('handler')
        else:
            self.conn.client_setname('generator')

    def executeTask(self):
        if self.conn.client_getname() == 'handler':
            self.getMessage()
        else:
            self.postMessage()

    def messageGenerator(self,size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def postMessage(self):
        return self.conn.rpush("messages",self.messageGenerator())

    def getMessage(self):
        message = self.conn.rpop("messages")
        if (random.uniform(0, 100) > 95):
            self.setError(message)

    def setError(self, message):
        return self.conn.rpush("errors", message)


