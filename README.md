# redisTest
"python3 main.py" for performing  basic tasks, "python3 main.py getErrors" for viewing error log.
# TODO
Correct realisation of pipeline for get method.

Error:
  AttributeError: 'NoneType' object has no attribute 'decode'. Theory: Sometimes message is None, somehow ignoring "pipe.exists("message")".
