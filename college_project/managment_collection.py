class ManagementCollection:
    """
    A collection of methods for lists management.
    """
    def __init__(self):
        self.__lst = []

    def add(self, instance):
        self.__lst.append(instance)

    def get(self, instance):
        return instance  # to use the __reaper__ in order to get all the details.

    def remove(self, instance):
        self.__lst.remove(instance)

    def print_all(self, instance):
        print(instance)  # to use __reaper__ or __str__
