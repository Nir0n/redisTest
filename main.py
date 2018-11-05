#!/usr/bin/python
from application import Application
import sys

def main():
    try:
        app=Application()
        if (sys.argv[1] == 'getErrors'):
            pipe = app.conn.pipeline()
            pipe.multi()
            pipe.lrange("errors", 0, - 1)
            pipe.ltrim("errors", 0, -1)
            pipe.delete("errors")
            errors=pipe.execute()
            if errors[2]:
                print([e.decode('utf-8') for e in errors[0]])
            else:
                print("Записей в архиве нет")
    except IndexError:
        while True:
            app.searchForRole()
            app.executeTask()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        print(ex)

main()