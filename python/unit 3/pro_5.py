class Temperature:
    def convertFahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def convertCelsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

t = Temperature()
print(t.convertFahrenheit(25))
print(t.convertCelsius(77))

# Output:
# 77.0
# 25.0
