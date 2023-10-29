class Item:
        """
        A class representing an item with a name and a category
        """
        def __init__(self, item_name, category):
            """
            Initializes a new item object with the given parameters
            - item_name: the name of the item
            - category: the category of the item
            """
            self.item_name = item_name
            self.category = category
            
        def set_name(self, new_name):
            """
            Changes the name of an item object
            - new_name: new name of item
            """
            self.item_name = new_name 

        def set_category(self, new_category):
            """
            Changes the category of an item object
            - new_category: new category of item
            """
            self.category = new_category

        def __str__(self)->str:
            """
            Returns a string representation of the object
            - item_name: the name of item
            - category: category of item
            """
            return f"Name: {self.item_name}, Category: {self.category}"















