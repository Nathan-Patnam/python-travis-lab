import pytest
from dfa import *


class TestDFA(object):
        @pytest.fixture(scope="function")
        def create_dfa(self,):
                test_dfa = build_dfa("./mocks/dfa/mock_dfa.txt")
                return test_dfa

        def test_states(self, create_dfa):
                states = set(["q2", "q1"])
                test_dfa_states = create_dfa.states
                assert states == test_dfa_states

        def test_alphabet(self, create_dfa):
                alphabet = set(["a", "b"])
                test_dfa_alphabet = create_dfa.alphabet
                assert alphabet == test_dfa_alphabet

        def test_start_state(self, create_dfa):
                start_state = "q1"
                test_dfa_state_state = create_dfa.start_state
                assert start_state == test_dfa_state_state

        def test_accept_state(self, create_dfa):
                accept_states = set(["q2"])
                test_dfa_accept_states = create_dfa.accept_states
                assert accept_states == test_dfa_accept_states

        def test_transitions(self, create_dfa):
                transitions = {"q1": {"a": "q2", "b": "q1"},
                            "q2": {"a": "q2", "b": "q2"}}
                test_dfa_transitions = create_dfa.transitions
                assert transitions == test_dfa_transitions


"""

def sum(num1, num2):
It returns sum of two numbers
    return num1 + num2

paramaterize tests -> test multiple sets of inputs at once
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

@pytest.mark.parametrize('num1, num2, expected',get_sum_test_data())
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected

@pytest.fixture
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]
        
def test_sum(get_sum_test_data):
        for data in get_sum_test_data:
                num1 = data[0]
                num2 = data[1]
                expected = data[2]
                assert sum(num1, num2) == expected

"""
