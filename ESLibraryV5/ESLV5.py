#ES Library V5 (2025 Edition)
#Passionately developed since 2023, it's purpose is to aid console-centric programming
#by adding fun cosmetics and debug features.

#Global Variables
TEXT_COLORS = {
    'RED' : ['\033[31m,\033[0m'],
    'GREEN' : ['\033[32m,\033[0m'],
    'YELLOW' : ['\033[33m,\033[0m'],
    'BLUE' : ['\033[34m,\033[0m'],
    'MAGENTA' : ['\033[35m,\033[0m'],
    'CYAN' : ['\033[36m,\033[0m'],
    'WHITE' : ['\033[37m,\033[0m'],
    'BOLD' : ['\033[1m,\033[0m'],
    'NONE' : ["\033[0m", "\033[0m"]
}

#Global Functions
def apply_text_effect(text, effect):
    assert type(text) == str, "apply_text_effect 'text' must be a string."
    assert effect.upper() in TEXT_COLORS.keys(), f"apply_text_effect 'effect' must be in [{', '.join(TEXT_COLORS.keys())}]"
    return TEXT_COLORS[effect][0] + text + TEXT_COLORS[effect][1]
def create_paragraph(text, max_length, indent = True):
    terms = text.split()
    if indent:
        temp_terms = ["  "]
        chara_total = 4
    else:
        temp_terms = []
        chara_total = 0
    allowed_error = round(max_length * 0.05)
    result_lines = []
    for term in terms:
        if chara_total >= max_length - allowed_error:
            chara_total = 0
            temp_terms.append(term)
            result_lines.append(' '.join(temp_terms))
            temp_terms = []
        else:
            temp_terms.append(term)
            chara_total += len(term)
    result_lines.append(' '.join(temp_terms))
    return result_lines
def create_header(header, width):
    bar_length = (width + len(header)) // 2
    bar = "=" * bar_length
    return f"{bar}[{header}]{bar}"

#Feature: There's a bot in my console!
class TABIMC():
    BOTS = {}
    #   'Keys' are names
    #   'Items' are objects
    def __init__(self, name = "Console Bot", title = "<TABIMC>", action_message = "is reporting"):
        self.name = str(name)
        self.title = str(title)
        self.action_message = str(action_message)
        TABIMC.BOTS[self.name] = self
    def tell(self,msg):
        #All message processing should occur here.
        result_message = ""
        if self.title != "":
            result_message += self.title + " "
        result_message += self.name + " "
        if self.action_message != "":
            result_message += self.action_message + " "
        result_message += str(msg)
        return result_message
    def say(self, msg):
        print(self.tell(msg))
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = str(title)
    def access_bot(name):
        return TABIMC.BOTS[name]
    def __str__(self):
        return f"{self.title} {self.name}"

#Feature: Function Sandbox (NEW!)

#Feature: The Sexy Nav Menu (NEW!)
#This may or may not make your life easier, I have no idea.
class TSNM_Menu():
    MENUS = {}
    #   'Keys' are menu identifiers
    #   'Items' are menu objects
    def __init__(self, identifier, width = 40):
        assert type(width) == int, "TSNM_Menu 'bar_length' must be an integer."
        self.id = str(identifier)
        self.width = width
        self.pages = {}
        #   'Keys' are page identifiers
        #   'Items' are page objects
        self.current_page_id = None
        self.current_page = None
    def add_page(self, identifier, header):
        temp_page = TSNM_Page(self, identifier, header)
        self.pages[str(identifier)] = temp_page
    def get_page(self, page_id):
        assert page_id in self.pages.keys(), f"{self.id} has no such page: {page_id}"
        return self.pages[page_id]
    def load_page(self, page_id):
        assert page_id in self.pages.keys(), f"{self.id} has no such page: {page_id}"
        self.current_page_id = page_id
        self.current_page = self.pages[page_id]
    def update(self):
        if self.current_page_id is not None:
            self.current_page.display_page()
            self.current_page.run_page()

class TSNM_Page():
    def __init__(self, menu_object, identifier, header):
        menu_object.pages[str(identifier)] = self
        self.id = str(identifier)
        self.menu = menu_object

        self.header = str(header)
        self.max_line_length = (len(self.header)) + (self.menu.width)
        self.description = ""

        self.inputs = []
        self.input_contexts = []
        self.input_handlers = []

        self.function = None
    def set_header(self, header):
        self.header = str(header)
        self.max_line_length = (len(self.header)) + (self.menu.width)
    def set_description(self, description):
        self.description = str(description)
    def add_input(self, input_name, input_context = None, input_handler = None):
        assert type(input_handler) == type(apply_text_effect), "An 'input_handler' must be a function."

        self.inputs.append(input_name)
        self.input_contexts.append(input_context)
        self.input_handlers.append(input_handler)
    def set_function(self, func):
        assert type(func) == type(apply_text_effect), "set_function's 'func' must be a function."
        self.function = func
    def display_page(self):
        print(create_header(self.header, self.max_line_length))

        for line in create_paragraph(self.description, self.max_line_length):
            print(line)
    def run_page(self):
        if self.function != None:
            user_inputs = []
            for i, needed_input in enumerate(self.inputs):

                if self.input_contexts[i] is not None:
                    for line in create_paragraph(self.input_contexts[i], self.max_line_length):
                        print(line)

                current_input = None
                input_invalid = True
                while input_invalid:
                    current_input = input(f"Enter {needed_input}: ")
                    if self.input_handlers[i] == None:
                        input_invalid = False
                    else:
                        input_invalid = not self.input_handlers[i](current_input)

                user_inputs.append(current_input)
            self.function(*user_inputs)
#Unit Testing (NEW!)