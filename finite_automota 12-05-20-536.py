class FiniteAutomota():
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