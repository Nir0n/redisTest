import string
import random
import asyncio
from redis.exceptions import WatchError

def messageGenerator(size=10, chars=string.ascii_uppercase + string.digits):
    asyncio.sleep(.500)
    return ''.join(random.choice(chars) for _ in range(size))

def postMessage(conn):
    conn.set("message",messageGenerator())

def getMessage(conn):
    message=conn.get("message")
    if message is not None:
        setError(conn, message)
        conn.delete("message")
        print("get")
    else:
        print("Сообщения еще нет")

# def getMessage(conn):
#     with conn.pipeline() as pipe:
#         try:
#             pipe.watch("message")
#             if pipe.exists("message"):
#                 pipe.multi()
#                 if (random.uniform(0, 100) > 95):
#                     if (pipe.get("errors") is None):
#                         print("error")
#                         pipe.set("errors", pipe.get("message"))
#                 pipe.delete("message")
#             print("del")
#             return pipe.execute()
#         except WatchError:
#             print("Сообщения еще нет")



def setError(conn, message):
    if (random.uniform(0, 100)>95):
        errors = (conn.get("errors"))
        if(errors is None):
            errors = message
        else:
            errors = errors.decode("utf-8") + " " + message.decode("utf-8")
        print("error")
        return conn.set("errors",errors)