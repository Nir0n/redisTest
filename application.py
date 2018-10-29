from connection import r
from main_tasks import postMessage, getMessage

class Application(object):
    def __init__(self):
        self.conn = r

    def searchForRole(self):
        clientsList=r.client_list()
        clientsRole=[d['name'] for d in clientsList if 'name' in d]
        if ('generator' in clientsRole):
            if(self.conn.client_getname() != 'generator'):
                self.conn.client_setname('handler')
        else:
            self.conn.client_setname('generator')

    def executeTask(self):
        if self.conn.client_getname() == 'handler':
            getMessage(self.conn)
        else:
            print("post")
            postMessage(self.conn)


