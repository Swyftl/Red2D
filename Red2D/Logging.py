import time


class Logging:

    def __init__(self, isDebug):
        self.isDebug = isDebug
        self.logLevels = ["Log", "Error", "Critical"]

        if isDebug:
            self.logFile = open("GameLog.log", "w+")
        else:
            pass

    def log(self, text, **kwargs):
        if "level" in kwargs:
            level = kwargs.get("level")
        else:
            level = "Log"
        if self.isDebug:
            match level:
                case "Log":
                    self.logFile.write("Log: "+text)
                case "Error":
                    self.logFile.write("Error: "+text)
                case "Critical":
                    self.logFile.write("Critical: "+text)
                case _:
                    self.logFile.write("Log: "+text)
                    self.log("Invalid Level for Above Log", level="Critical")