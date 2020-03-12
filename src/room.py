class Room:
    def __init__(self,name,description,item = None):
        self.name = name
        self.description = description
        self.item = [item]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f'{self.name}, {self.description} on the ground theres a....{self.item}!'.format(self=self)