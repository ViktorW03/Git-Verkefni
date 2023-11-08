class Catalog:
    """
    A class representing a catalog with a name and a list of items
    """     
    def __init__(self, catalog_name)->None:
        """
        Initializes a new catalog object with the given parameters
        """
        self.catalog_name = catalog_name
        self.items = []

    def add(self, item)->None:
        self.items.append(item)

    def remove(self, item)->None:
        self.items.remove(item)

    def set_name(self, new_name)->None:
        self.catalog_name = new_name

    def clear(self)->None:
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
