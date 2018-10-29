#!/usr/bin/python
from application import Application
import sys

def main():
    try:
        app=Application()
        if (sys.argv[1] == 'getErrors'):
            if app.conn.get("errors"):
                print(app.conn.get("errors").decode("utf-8"))
                app.conn.delete("errors")
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