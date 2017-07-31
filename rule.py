class rule:

    def __init__(self, expression):
        #Instance variables
        self.EXPRESSION = expression
        self.action = None
        self.subject = None
        self.info = ""
        #self.NEXT_EXPECTED_TYPE = {'EXP', 'ACT', 'SUB', 'INFO'}

    def set_action(self, action):
        self.action = action

    def set_subject(self, subject):
        self.subject = subject

    def set_info(self, info):
        self.info = info

    def append_info(self, info):
        self.info += info

    def get_expression(self):
        return self.EXPRESSION

    def get_action(self):
        return self.action

    def get_subject(self):
        return self.subject

    def get_info(self):
        return self.info
