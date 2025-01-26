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
                    print(f"\32Log: {text}\33[0m")
                    self.logFile.write("Log: "+text+"\n")
                case "Error":
                    print(f"\33[91mError: {text}\31[0m")
                    self.logFile.write("Error: "+text+"\n")
                case "Critical":
                    print(f"\33[31mCritical: {text}\33[0m")
                    self.logFile.write("Critical: "+text+"\n")
                case _:
                    print(f"\32Log: {text}\33[0m")
                    self.logFile.write("Log: "+text+"\n")
                    self.log("Invalid Level for Above Log", level="Critical")