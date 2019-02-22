import pytest
from dfa import *


def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2



"""
paramaterize tests -> test multiple sets of inputs at once
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

@pytest.mark.parametrize('num1, num2, expected',get_sum_test_data())
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected


"""


@pytest.fixture
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]
        
def test_sum(get_sum_test_data):
        for data in get_sum_test_data:
                num1 = data[0]
                num2 = data[1]
                expected = data[2]
                assert sum(num1, num2) == expected


# class TestDFA(object):
#     def __init__(self):


#     @classmethod
#     def setup_class(cls):
#         test_dfa = build_dfa("./dfa_inputs/mock_dfa.txt")
#         print(test_dfa.states())

#     def setup_method(self, method):
#         """ setup any state tied to the execution of the given method in a
#         class.  setup_method is invoked for every test method of a class.
#         """
    







