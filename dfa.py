#can we assume valid input, valid alphabet,


class DFA():

    """Representation of a DFA

     Attributes:
        states set(str): all of the possible states of the machine
        alphabet set(str): all the different transitions the machine recognizes
        start_state (str): start state of the machine
        accept_states set(str): all of the end states of the machine
        transitions set(str): what each of the transitions are for the machine
    """

    def __init__(self):
        self.states = set()
        self.alphabet = ""
        self.start_state = ""
        self.end_states = ""
        self.transitions = {}
        
    def set_states(self, states):
        states = self.__turn_list_items_into_a_set(states)
        self.states = states

    def set_alphabet(self, alphabet):
        alphabet = self.__turn_list_items_into_a_set(alphabet)
        self.alphabet = alphabet

    def set_start_state(self, start_state):
        start_state = start_state.strip()
        self.start_state = start_state

    def set_accept_states(self, accept_states):
        accept_states = self.__turn_list_items_into_a_set(accept_states)
        self.accept_states = accept_states

    def __turn_list_items_into_a_set(self, line):
        line = line.strip()
        items = line.split(",")
        items = set(items)
        return items

    

    def run_machine(self, file_name, output_file):
        """ takes in a file of sequences, and checks to see if each sequnece will be accepted or rejceted by the machine
        Args:
            file_name: file to read sequences from
            output_file: file to write whether each sequnce will be rejected or accepted to
        Returns:
            None
        """
        results = []
        #iterate through each string in the input and calculate the final state
        with open(file_name, 'r+') as fh:
            for record in fh:
                current_state = self.start_state
                record = record.strip()
                for transition in record:
                    if transition in self.alphabet:
                        current_state = self.__get_transition_state(
                            current_state, transition)
                #checks to see if final state is a accepted state by the machine
                if self.state_is_an_accept_state(current_state):
                    results.append("Accept\n")
                else:
                    results.append("Reject\n")
        self.__save_results_to_file(results, output_file)

    def __get_transition_state(self, start_state, transition):
        if start_state in self.transitions:
            if transition in self.transitions[start_state]:
                return self.transitions[start_state][transition]

    def __save_results_to_file(self, results, file_name):
        with open(file_name, "w") as fh:
            for result in results:
                fh.write(result)

    def state_is_an_accept_state(self, state):
        return state in self.accept_states

    def add_transitsion(self, transition):
        #algorithm create dictionary where each key is a state that maps to another dictionary where each key is a transition and value is another state -> {a: {1: "b"}}

        transition = transition.strip()
        transition = transition.split(",")
        start_state = transition[0]
        transition_letter = transition[1]
        end_state = transition[2]
        if start_state not in self.transitions:
            self.transitions[start_state] = {}
        self.transitions[start_state][transition_letter] = end_state


def main():
    dfa = build_dfa("./mocks/dfa/mock_dfa.txt")
    dfa.run_machine("./input.txt", "output.txt")


def build_dfa(file_name):
    """Build dfa from a file

        Args:
            file_name : file you want to get data from
        
        Returns:
            representation of a dfa

        File Requirements
        Line 1: the states of the DFA (separated by commas, if there is more than one state)
	    Line 2: the alphabet of the DFA (separated by commas, if there is more than one symbol)
	    Line 3: the starting state of the DFA
	    Line 4: the final/accept states of the DFA (separated by commas, if there is more than one accept state)
	    Line 5 and onward: the transition rules 
        """
    dfa = DFA()
    with open(file_name, 'r+') as fh:
        line_number = 1
        for line in fh:
            # states of DFA
            if line_number == 1:
                dfa.set_states(line)
            elif line_number == 2:
                 dfa.set_alphabet(line)
            elif line_number == 3:
                 dfa.set_start_state(line)
            elif line_number == 4:
                dfa.set_accept_states(line)
            else:
                dfa.add_transitsion(line)
            line_number += 1
    return dfa


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
