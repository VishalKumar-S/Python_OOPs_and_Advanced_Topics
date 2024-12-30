import logging
print("Logging is done to  perform debugging and to perform RCA (Root Cause Analysis), and to provide statistics like no of requests per day. There are 6 logging levels in Python. They are:\n1) Critical- Value: 50 \n2) Error- Value: 40 \n3) Warning- Value: 30 \n4) Info- Value: 20 \n2) Debug- Value: 10 \n1) NotSet- Value: 0.\n We can access these values either by their names or by their values. By default, Python gives level Warning. We can modifyf our default Warning level. We would be able to use that certain default level, and all the levels above it. For e.,g if byd defualt logging level is Warning, then we can access warning, error and critical levels. NotSet level refers to there is no logging implemented. By default, the log file appends the new logs in it,if u want to override, then modify the file mode")

  

print("If u want to save it in a file: ")
logging.basicConfig(filename = "C:/Users/HP/Downloads/College/asd.txt",level = logging.DEBUG)
logging.debug("Debug warning")
logging.info("Info warning")
logging.warning("Warning warning")
logging.error("Error warning")
logging.critical("Critical warning")

print("If u want to override the existing log file data, change the file mode like: 'logging.basicConfig(filename = 'C:/Users/HP/Downloads/College/asd.txt',level = logging.DEBUG, filemode = 'w')'\n If u want to print the logging statements, directly in the console itself, then just use simply 'logging.basicConfig()'")

print("To modify the format in the loggging statements,use format for e.,g")
print("logging.basicConfig(filename = 'C:/Users/HP/Downloads/College/asd.txt',level = logging.DEBUG, format = %(asctime)s:%(levelname)s:%(message)s,datefmt = '%d/%m/%Y: %I/%M:%S %p') would give output in the format\n 30/12/2024 4:17:00 PM:DEBUG:Debug warning\n just format = %(asctime)s:%(levelname)s:%(message)s woudl give us \n 2024/12/30 4:17:00 PM:DEBUG:Debug warning\n just format = %(levelname)s gives us \n DEBUG \n just format = %(message)s gives us \n Debug warning")