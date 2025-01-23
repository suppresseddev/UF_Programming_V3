#ESLV4
#Passionately developed since 2023, it's purpose is to aid console-centric programming
#by adding fun cosmetics and debug features.
libheader = "[ESLV4] "
indent = " "*(len(libheader))
debug = True
if debug:
    alerttiers = {
        1 : "PROGRAM ERROR", #Something regarding your code is fundamentally broken.
        2 : "CRITICAL ERROR", #Your code functioned as intended, but what you intend is impossible.
        3 : "SOFT ERROR", #Your code is probably not functioning as intended.
        4 : "NOTICE" #Your intentions are stupid, probably.
    }
    print(f"{libheader}DEBUG MODE ENABLED")
def alert (type):
    print(f"{indent}[!]{alerttiers[int(type)]}[!]")
#Functions
#This section pertains to enhancing functions in python.
import inspect
def examplefunction():
    print("Example Function Ran Successfully")
    print(examplefunction.__name__)
functionclass = type(examplefunction)

#The 'debug' function allows you to quickly and easily debug at any given point in your project.
def debug(self, msg=""):
    func = inspect.currentframe().f_back.f_code.co_name
    variables = locals()
    # Always use format-strings, kids.
    print(f"{libheader}Error in function/method -> <{func}>\n{indent}<{func}> is reporting -> {msg}\n{indent}Objects In Play -> {variables}")
#There's a Bot In My Console!
#Give your console-based python projects a bit more life.
class TABIMC:
    def __init__(self, name = "Console Bot", role = "[TABIMC]", notif = "is reporting"):
        self.name = str(name)
        self.role = role
        self.notif = notif
        self.msg = ""
    def say(self, msg = ""):
        self.msg = str(msg)
        print(f"{libheader}{self.name} {self.notif} -> {self.msg}")
    def tell(self, msg = None):
        if msg != None:
            self.msg = str(msg)
        return(f"{libheader}{self.name} {self.notif} -> {self.msg}")
    def debug(self, msg = ""):
        func = inspect.currentframe().f_back.f_code.co_name
        variables = locals()
        #Always use format-strings, kids.
        print(f"{libheader}Error in function/method -> <{func}>\n{indent}<{func}> is reporting -> {msg}\n{indent}Objects In Play -> {variables}")
    def verify(self):
        if self.name == "":
            alert(4)
            self.say("The name of this bot is '' which is not good for aesthetics.")

# bot = TABIMC("","[TABIMC]", "is reporting")
# bot.say("Gello Gorld.")
# def testfunction():
#     print(214)
#     bot.debug("This is a test.")
# bot.verify()
# bot.name = "Fixed"
# bot.verify()
# bot.say("I have fixed the issue.")
# testfunction()
class FunctionSandbox:
    def __init__(self, function):
        self.function = function
        self.inputsettings = []

#The Sexy Nav Manu V2
#Basically, a tool to create the sexiest python console projects you've ever seen.
class TSNM:
    def __init__(self, name = "Main Menu"):
        self.name = str(name)
        self.headerlength = 30
        self.pageTitle = []
        self.pageDesc = []
    def header(self, heading = ""):
        bar = "="*int((self.headerlength/2))
        print(f"{bar}{heading}{bar}")