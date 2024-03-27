"""
Example of class method
Suppose you have a class representing different units of measurement, and you want to create methods to convert between them.
You might use a class method to achieve this because the conversion factor might be related to the class itself rather than a specific instance.
In this example, the conversion factors are related to the class itself (Measurement). Therefore, it makes sense to use class methods for conversion operations.
"""


class Measurement:
    # Conversion factors
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 0.621371

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    @classmethod
    def miles_to_kilometers(cls, miles):
        return miles * cls.MILES_TO_KM

    @classmethod
    def kilometers_to_miles(cls, km):
        return km * cls.KM_TO_MILES


# Using class methods to convert measurements
print("5 miles in kilometers:", Measurement.miles_to_kilometers(5))  # Output: 8.0467
print("10 kilometers in miles:", Measurement.kilometers_to_miles(10))  # Output: 6.21371
