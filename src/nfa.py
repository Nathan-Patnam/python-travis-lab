class NFA():
    def __init__(self):
        self.states = set()
        self.alphabet = ""
        self.start_state = ""
        self.end_states = set()
        self.transitions = {}

    def set_states(self, states):
        states = self.__turn_list_items_into_a_set(states)
        self.__add_states_to_transitions(states)
        self.states = states

    def set_alphabet(self, alphabet):
        alphabet = self.__turn_list_items_into_a_set(alphabet)
        self.alphabet = alphabet

    def set_start_state(self, start_state):
        start_state = start_state.strip()
        self.start_state = start_state

    def set_accept_states(self, accept_states):
        accept_states = self.__turn_list_items_into_a_set(accept_states)
        self.end_states = accept_states

    def __turn_list_items_into_a_set(self, line):
        line = line.strip()
        items = line.split(",")
        items = set(items)
        return items

    def __add_states_to_transitions(self, states):
        for state in states:
            self.transitions[state] = {}

    def get_children(self, state):
        return self.transitions[state]

    def get_output(self, input_string):
        start_state = self.start_state
        result = self.__get_output(start_state, input_string)
        if result:
            return "accept"
        else:
            return "reject"

    def __get_output(self, current_state, input_string):

        # base condition -> 0 char left and current state in a final state
        if input_string == "" and self.state_is_an_accept_state(current_state):
            return True

        # check to see if there are any empty transitions in the start state
        if "@" in self.transitions[current_state]:
            for transition in self.transitions[current_state]["@"]:
                # make sure I am not transitioning to the same step infinitely
                if transition != current_state:
                    if self.__get_output(
                            transition, input_string):
                        return True

        if len(input_string) >= 1:
            transition = input_string[0]
            input_string = input_string[1:]
            if transition in self.transitions[current_state]:
                for trans_state in self.transitions[current_state][transition]:
                    if self.__get_output(trans_state, input_string):
                        return True
        return False

    def run_machine(self, file_name, output_file):
        """ takes in a file of sequences, and checks to see
        if each sequnece will be accepted or rejceted by the machine
        Args:
            file_name: file to read sequences from
            output_file: file to write whether each sequnce will be
            rejected or accepted to
        Returns:
            None
        """
        results = []
        # iterate through each char in the input and calculate the final state
        with open(file_name, 'r') as fh:
            for input_string in fh:
                input_string = input_string.strip()
                result = self.get_output(input_string)
                results.append(result)
        self.__save_results_to_file(results, output_file)

    def __save_results_to_file(self, results, output_file):
        with open(output_file, "w") as fh:
            for result in results:
                fh.write(result + "\n")

    def state_is_an_accept_state(self, state):
        return state in self.end_states

    def add_transitsion(self, transition):
        # algorithm create dictionary where each key is a state that maps
        # to another dictionary where each key is a transition
        # state -> {a: {1: "b"}}
        transition = transition.strip()
        transition = transition.split(",")
        start_state = transition[0]
        transition_letter = transition[1]
        end_state = transition[2]
        if transition_letter not in self.transitions[start_state]:
            self.transitions[start_state][transition_letter] = [end_state]
        else:
            self.transitions[start_state][transition_letter].append(end_state)


def main():
    nfa = build_nfa("./mocks/nfa_1.txt")
    nfa.run_machine("./mocks/nfa_input_1.txt", "./output.txt")


def build_nfa(file_name):
    """Build an NFA from a file

        Args:
            file_name : file you want to get data from

        Returns:
            representation of a dfa

        File Requirements
        Line 1: the states of the DFA (separated by commas,
        if there is more than one state)
            Line 2: the alphabet of the DFA (separated by commas,
            if there is more than one symbol)
            Line 3: the starting state of the DFA
            Line 4: the final/accept states of the DFA (separated by commas, if
            there is more than one accept state)
            Line 5 and onward: the transition rules
        """
    nfa = NFA()
    with open(file_name, 'r+') as fh:
        line_number = 1
        for line in fh:
            if line_number == 1:
                nfa.set_states(line)
            elif line_number == 2:
                nfa.set_alphabet(line)
            elif line_number == 3:
                nfa.set_start_state(line)
            elif line_number == 4:
                nfa.set_accept_states(line)
            else:
                nfa.add_transitsion(line)
            line_number += 1
    return nfa


if __name__ == "__main__":
    main()
