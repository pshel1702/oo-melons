"""Classes for melon orders."""

import random

class AbstractMelonOrder:
    shipping = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Get base price based on splurge pricing."""
        self.base_price = random.randrange(4,10)
        return self.base_price
    
    def get_total(self):
        """Calculate price, including tax."""
        self.base_price = self.get_base_price()
        print(self.base_price)
        total = ((1 + self.tax) * self.qty * self.base_price) + self.shipping

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True




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



  


