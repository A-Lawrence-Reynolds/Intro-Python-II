class Room:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.item = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        total_items = ''
        for i in self.item:
            total_items += ", " + i.name
        return f'{self.name}, {self.description} on the ground theres a....{total_items}!'

    # def get_room_items(self):
    #     for item in self.item