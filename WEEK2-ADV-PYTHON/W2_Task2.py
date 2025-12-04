# Task 2 — Encapsulation (Single underscore)
# Instructions
# 1. Create a class TemperatureSensor.
# 2. It must contain:
# ○ An internal attribute _celsius
# ○ A public method set_celsius(value) that ensures the value is a float
# and stores it
# ○ A public method get_fahrenheit() that converts _celsius to
# Fahrenheit and returns it
# 3. External code must not access _celsius directly.
class TemperatureSensor:
    def __init__(self):
        self._celsius = 0.0

    def set_celsius(self, value):
        try:
            self._celsius = float(value)
        except ValueError:
            raise ValueError("Temperature must be a float")

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32
# Example usage
if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.set_celsius(25)
    fahrenheit = sensor.get_fahrenheit()
    print(f"The temperature in Fahrenheit is {fahrenheit}")