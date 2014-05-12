# coding=utf-8

class KBException(Exception):
    def __init__(self, message, line=None):
        Exception.__init__(self, message)
        self.line = line

    def __str__(self):

        if self.line is None:
            return self.message

        return "Error at line #%d:\n%s" % (self.line, self.message)


class KBQuestionParseException(KBException):
    pass


class KBRuleParseException(KBException):
    def __init__(self, message, line=None, rule_line=None, rule_lines=None):
        KBException.__init__(self, message, line)
        self.rule_line = rule_line
        self.rule_lines = rule_lines

    def __str__(self):
        if self.rule_line is None or self.rule_lines is None:
            return KBException.__str__(self)

        if self.line is not None:
            self.line -= self.rule_lines + self.rule_line - 1

        return KBException.__str__(self)