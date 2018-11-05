from connection import r
import string
import random
import logging

class Application(object):

    def __init__(self):
        self.conn = r
        self.set_app_logger()

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
            logging.info("Get sequence start")
            self.getMessage()
            logging.info("Get sequence complete")
        else:
            logging.info("Post sequence start")
            self.postMessage()
            logging.info("Post sequence complete")

    def messageGenerator(self,size=10, chars=string.ascii_uppercase + string.digits):
        message=''.join(random.choice(chars) for _ in range(size))
        logging.info("Post message: " + message)
        return message

    def postMessage(self):
        return self.conn.rpush("messages",self.messageGenerator())

    def getMessage(self):
        message = self.conn.lpop("messages")
        logging.info("Get message: " + message.decode("utf-8"))
        if (random.uniform(0, 100) > 95):
            self.setError(message)
            logging.info("Error set" + message.decode("utf-8"))

    def setError(self, message):
        return self.conn.rpush("errors", message)

    def set_app_logger(self):
        logger=logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s',
                                        level=logging.INFO)
        return logger


