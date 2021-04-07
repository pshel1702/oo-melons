"""Classes for melon orders."""

from random import Random

class AbstractMelonOrder:
    shipping = 0
    base_price = get_base_price(self)

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_total(self):
        """Calculate price, including tax."""
        print(self.base_price)
        total = ((1 + self.tax) * self.qty * self.base_price) + self.shipping

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_base_price(self):
        """Get base price based on splurge pricing."""

       return self.base_price = random(4,10)




class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self,species,qty):
        super().__init__(species,qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty)
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code
        if self.qty < 10 :
            self.shipping = 3
        else:
            self.shipping = 0
         
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticChristmasMelonOrder(DomesticMelonOrder):
    """A domestic christmas melon order"""

    def __init__(self,name,qty):
        """Set initial attributes of Domestic Christmas Melons."""
        super().__init__(name,qty)
        self.base_price = 1.5 * self.base_price

class InternationalChristmasMelonOrder(InternationalMelonOrder):
    """An international christmas melon order."""

    def __init__(self,name,qty,country_code):
        """Set initial attributes of International Christmas Melons."""
        super().__init__(name,qty,country_code)
        self.base_price = 1.5 * self.base_price

class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government Melon Order"""

    def __init__(self,name,qty):
        """Set initial attributes of an order set for government inspection"""
        super().__init__(name,qty)
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self,passed):
        """Inspect a melon and set inspection status to true"""

        self.passed_inspection = passed



  


