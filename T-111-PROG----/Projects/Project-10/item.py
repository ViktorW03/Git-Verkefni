class Item:
        """
        A class representing an item with a name and a category
        """
        def __init__(self, item_name, category)->None:
            """
            Initializes a new item object with the given parameters
            """
            self.item_name = item_name
            self.category = category
            
        def set_name(self, new_name)->None:
            self.item_name = new_name 

        def set_category(self, new_category)->None:
            self.category = new_category

        def __str__(self)->str:
            """
            Returns a string representation of  the object
            """
            return f"Name: {self.item_name}, Category: {self.category}"















