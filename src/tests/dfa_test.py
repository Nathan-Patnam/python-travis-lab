import sys
sys.path.append(sys.path[0] + "/..")
from ..dfa import build_dfa, DFA  # noqa: E402
import pytest  # noqa: E402


class TestDFAMOCK(object):
        def test_build_dfa(self):
                dfa = DFA()
                dfa.set_states("q1,q2")
                dfa.set_alphabet("a,b")
                dfa.set_start_state("q1")
                dfa.set_accept_states("q2")
                INPUT_FILE = "./mocks/dfa_input_1.txt"
                OUTPUT_FILE = "./mocks/outputs/dfa_output_1.txt"
                dfa.run_machine(INPUT_FILE, OUTPUT_FILE)

                assert dfa.state_is_an_accept_state("q2")


class TestDFA(object):
        @pytest.fixture(scope="function")
        def create_dfa(self,):
                test_dfa = build_dfa("./mocks/dfa_1.txt")
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
