from models.group import Group

class GroupController:

    def __init__(self):
        self.groups = []

    def add_group(self, idGroup, course, teacher, maxCapacity, schedule):
        group = Group(idGroup, course, teacher, maxCapacity, schedule)
        self.groups.append(group)
        return group

    def get_groups(self):
        return self.groups.copy()

    def find_group(self, idGroup):
        for group in self.groups:
            if group.get_idGroup() == idGroup:
                return group
        return None