class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp = []

        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00

        temp.append(kelvin)
        temp.append(fahrenheit)

        return temp
