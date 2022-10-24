class Table:

    def __init__(self, slots):
        self._slots = []
        self._max_slots = slots

    def add_slot(self, value):
        if value == self._max_slots:
            return True
        elif value in self._slots:
            self._slots = []
            return False
        else:
            self._slots.append(value)
            return True

    def get_coins(self):
        return len(self._slots)

    def clear_coins(self):
        self._slots = []

    def print_coins(self):
        """
            ####################
            # 1 # 2 # 3 # 4 # 5 #
            ####################
        """
        print("####################")
        for slot in self._slots:
            print(f"# {slot} ", end="")
        print("#")
        print("####################")