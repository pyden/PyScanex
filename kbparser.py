# coding=utf-8

import re
from parser_exceptions import KBQuestionParseException, KBRuleParseException
from settings import KEYWORDS
from patterns import REGEXP_QUESTION_PATTERN, REGEXP_RULE_NUMBER_PATTERN, \
    REGEXP_RULE_START_PATTERN, REGEXP_RULE_PARAMETER_PATTERN, REGEXP_RULE_DECISION_PATTERN
import copy


class KBParser():
    def __init__(self):
        self.questionPattern = re.compile(REGEXP_QUESTION_PATTERN, re.VERBOSE)
        self.ruleNumberPattern = re.compile(REGEXP_RULE_NUMBER_PATTERN, re.VERBOSE)
        self.ruleStartPattern = re.compile(REGEXP_RULE_START_PATTERN, re.VERBOSE)
        self.ruleParameterPattern = re.compile(REGEXP_RULE_PARAMETER_PATTERN, re.VERBOSE)
        self.ruleDecisionPattern = re.compile(REGEXP_RULE_DECISION_PATTERN, re.VERBOSE)
        self.knowledgeBase = None


    def newKnowledgeBase(self):
        if self.knowledgeBase is not None:
            del self.knowledgeBase

        self.knowledgeBase = dict()
        self.knowledgeBase['parameters'] = dict()
        self.knowledgeBase['rules'] = dict()
        self.knowledgeBase['indexer'] = dict()


    def parse(self, fileName=None):

        if fileName is None:
            return

        try:
            kbFile = open(fileName, 'r')
        except IOError:
            raise

        kbEntity = ''
        lineNumber = 0

        self.newKnowledgeBase()

        try:
            for line in kbFile:
                lineNumber += 1
                if line.startswith(KEYWORDS['comment']):
                    continue

                if line == '\n':
                    if kbEntity == '':
                        continue

                    self.parseEntity(kbEntity)

                    kbEntity = ''
                    continue

                kbEntity += line

            if kbEntity != '':
                self.parseEntity(kbEntity)

        except KBQuestionParseException as e:
            raise KBQuestionParseException(str(e), lineNumber - 2)
        except KBRuleParseException as e:
            raise KBRuleParseException(str(e), line=lineNumber, rule_line=e.rule_line, rule_lines=e.rule_lines)

        kbFile.close()
        return copy.deepcopy(self.knowledgeBase)


    def parseEntity(self, entity=None):

        if entity is None:
            return

        if entity.startswith(KEYWORDS['question']):

            self.parseQuestion(entity)

        elif entity.startswith(KEYWORDS['rule']):

            self.parseRule(entity)

        elif entity.startswith(KEYWORDS['goal']):
            self.knowledgeBase['goal'] = entity.strip()[entity.index(' ') + 1:]

    def parseQuestion(self, qEntity):
        matches = self.questionPattern.match(qEntity)

        if matches is None:
            raise KBQuestionParseException("%s\nis not a valid question" % qEntity)

        self.addQuestion(matches.groupdict())


    def addQuestion(self, question=None):

        if question is None:
            return

        if question['parameter'] in self.knowledgeBase['parameters']:
            raise KBQuestionParseException("\"%s\" parameter redefinition" % question['parameter'])

        self.knowledgeBase['parameters'][question['parameter']] = {
            'question': question['text'],
            'values': set()
        }


    def addIndex(self, parameter=None, ruleNumber=None):

        if parameter is None:
            return

        if ruleNumber is None:
            return

        index = parameter['name'] + ":" + parameter['value']

        if index not in self.knowledgeBase['indexer']:
            self.knowledgeBase['indexer'][index] = set()

        self.knowledgeBase['indexer'][index].add(ruleNumber)

    def parseRule(self, ruleEntity):
        currLine = 0

        lines = ruleEntity.rstrip('\n').split('\n')

        match = self.ruleNumberPattern.match(lines[currLine])

        if match is None:
            raise KBRuleParseException('Rule number is not defined', rule_line=1, rule_lines=len(lines))

        ruleNumber = str(match.group(0))

        self.knowledgeBase['rules'][ruleNumber] = {
            'parameters': dict(),
            'decisions': dict()
        }

        currLine += 1

        match = self.ruleStartPattern.match(lines[currLine])
        if match is None:
            raise KBRuleParseException("Rule doesn't contains \"%s\"" % KEYWORDS['if'],
                                           rule_line=currLine + 1, rule_lines=len(lines))

        parameter = match.groupdict()
        if parameter['name'] not in self.knowledgeBase['parameters']:
            raise KBRuleParseException("Unknown parameter \"%s\"" % parameter['parameter'],
                                           rule_line=currLine + 1, rule_lines=len(lines))

        self.knowledgeBase['parameters'][parameter['name']]['values'].add(parameter['value'])
        self.knowledgeBase['rules'][ruleNumber]['parameters'][parameter['name']] = parameter['value']

        self.addIndex(parameter, ruleNumber)

        while True:
            currLine += 1

            if currLine == len(lines):
                raise KBRuleParseException("Not expected end of rule",
                                           rule_line=currLine + 1, rule_lines=len(lines))

            if lines[currLine].startswith(KEYWORDS['then']):
                break
            match = self.ruleParameterPattern.match(lines[currLine])
            if match is None:
                raise KBRuleParseException("Invalid syntax", rule_line=currLine + 1, rule_lines=len(lines))
            parameter = match.groupdict()
            self.knowledgeBase['parameters'][parameter['name']]['values'].add(parameter['value'])
            self.addIndex(parameter, ruleNumber)

        while True:
            if currLine == len(lines):
                break

            match = self.ruleDecisionPattern.match(lines[currLine])
            if match is None:
                raise KBRuleParseException("Invalid syntax", rule_line=currLine + 1, rule_lines=len(lines))

            decision = match.groupdict()
            self.knowledgeBase['rules'][ruleNumber]['decisions'][decision['name']] = decision['value']
            currLine += 1