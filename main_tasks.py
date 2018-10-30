import string
import random
import asyncio
from redis.exceptions import WatchError

def messageGenerator(size=10, chars=string.ascii_uppercase + string.digits):
    asyncio.sleep(.500)
    return ''.join(random.choice(chars) for _ in range(size))

def postMessage(conn):
    try:
        pipe=conn.pipeline()
        pipe.watch("message")
        return pipe.set("message",messageGenerator())
    except WatchError:
        print("Сообщение изменено во время выполнения операции")

def getMessage(conn):
    pipe=conn.pipeline()
    try:
        pipe.watch("message")
        if pipe.exists("message"):
            message=pipe.get("message")
            pipe.multi()
            print("get")
            setError(conn,message)
            pipe.delete("message")
            print("del")
            return pipe.execute()
    except WatchError:
        print("Сообщение удалено")

def setError(conn, message):
    if (random.uniform(0, 100)>95):
        errors = (conn.get("errors"))
        if(errors is None):
            errors = message
        else:
            errors = errors.decode("utf-8") + " " + message.decode("utf-8")
        print("error")
        conn.set("errors",errors)
