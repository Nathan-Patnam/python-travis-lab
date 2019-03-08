# Add this line to the beginning of relative.py file
import sys
sys.path.append(sys.path[0] + "/..")
import pytest
from src.nfa import build_nfa


class TestNFA(object):
    @pytest.fixture(scope="function")
    def create_nfa(self):
        test_nfa = build_nfa("mocks/nfa_1.txt")
        test_nfa.run_machine("./mocks/nfa_input_1.txt", "./mocks/outputs/nfa_output_1.txt")
        return test_nfa

    def test_get_states(self, create_nfa):
        states = set(["s2", "s1", "s3", "s4", "s5"])
        nfa_states = create_nfa.states
        assert states == nfa_states

    def test_get_alphabet(self, create_nfa):
        alphabet = set(["0", "1", "2"])
        nfa_alphabet = create_nfa.alphabet
        assert alphabet == nfa_alphabet

    def test_get_start_state(self, create_nfa):
        start_state = "s1"
        nfa_start_state = create_nfa.start_state
        assert start_state == nfa_start_state

    def test_get_end_states(self, create_nfa):
        end_states = set(["s3", "s5"])
        nfa_end_states = create_nfa.end_states
        assert end_states == nfa_end_states

    @pytest.fixture
    def get_machine_result_for_each_input(self):
        return [("012012", "accept"),
                ("000", "reject"),
                ("1", "accept"),
                ("22222222222222", "accept"),
                ("210012", "reject"),
                ("010101", "accept"),
                ("1111111111110", "accept")
                ]

    def test_inputs_on_state(self, create_nfa, get_machine_result_for_each_input):
        for input_output in get_machine_result_for_each_input:
                input_string = input_output[0]
                output = create_nfa.get_output(input_string)
                expected_output_string = input_output[1]
                assert output == expected_output_string

    @pytest.fixture
    def get_neighbors_for_each_state(self):
        return [("s1", {'@': ['s2', 's4']}),
                ("s2", {"0": ["s2"], "1":["s3"]}),
                ("s3", {"0": ["s3"], "1":["s3"], "2":["s3"]}),
                ("s4", {"1": ["s4"], "2":["s4", "s5"]}),
                ]

    def test_get_neighbors(self, create_nfa, get_neighbors_for_each_state):
        for state_neighbor_pair in get_neighbors_for_each_state:
                state = state_neighbor_pair[0]
                expected_neighbors = state_neighbor_pair[1]
                assert create_nfa.get_children(state) == expected_neighbors

  