class Catalog:
    """
    A class representing a catalog with a name and a list of items
    """     
    def __init__(self, catalog_name):
        """
        Initializes a new catalog object with the given name
        - catalog_name: the name of catalog
        - items: a list of items in catalog
        """
        self.catalog_name = catalog_name
        self.items = []

    def add(self, item):
        """
        Adds an item to catalog
        """
        self.items.append(item)

    def remove(self, item):
        """
        Removes an item from catalog
        """
        self.items.remove(item)

    def set_name(self, new_name):
        """
        Changes the name of catalog
        """
        self.catalog_name = new_name

    def clear(self):
        """
        Removes all items from catalog
        """
        if self.items:
            self.items.clear()
    
    def __str__(self)->str:
        """
        Returns a string representation of the catalog object
        """
   
        result = f"Catalog {self.catalog_name}:"
        for item in self.items:
                result += f"\n\t{item}"
        return result
