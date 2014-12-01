# coding=utf-8

import settings

REGEXP_QUESTION_PATTERN = r"""
        %s \s
        (?P<parameter>.+):\s
        (?P<text>.+\?) """ % (settings.KEYWORDS['question'])

REGEXP_RULE_NUMBER_PATTERN = r"""
    %s \s (?P<number> [\d]+\Z)
    """ % (settings.KEYWORDS['rule'])

REGEXP_RULE_START_PATTERN = r"""
    %s \s (?P<name> .+) \s %s \s (?P<value> .+)\Z
    """ % (settings.KEYWORDS['if'], settings.KEYWORDS['is'])

REGEXP_RULE_PARAMETER_PATTERN = r"""
    %s \s (?P<name> .+) \s %s \s (?P<value> .+)\Z
    """ % (settings.KEYWORDS['and'], settings.KEYWORDS['is'])

REGEXP_RULE_DECISION_PATTERN = r"""
    %s \s (?P<name> .+) \s %s \s (?P<value> .+)\Z
    """ % (settings.KEYWORDS['then'], settings.KEYWORDS['is'])
