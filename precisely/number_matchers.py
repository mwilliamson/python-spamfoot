import operator

from .results import matched, unmatched


def greater_than(value):
    return ComparisonMatcher(operator.gt, "greater than", value)


def _comparison_matcher(operator, operator_description, value):
    return ComparisonMatcher(operator, operator_description, value)


class ComparisonMatcher(object):
    def __init__(self, operator, operator_description, value):
        self._operator = operator
        self._operator_description = operator_description
        self._value = value

    def match(self, actual):
        if self._operator(actual, self._value):
            return matched()
        else:
            return unmatched("was {0!r}".format(actual))

    def describe(self):
        return "{0} {1!r}".format(self._operator_description, self._value)
