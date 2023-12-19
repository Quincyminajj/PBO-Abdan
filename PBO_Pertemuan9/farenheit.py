#Terstruktur
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def fahrenheit_to_reamur(fahrenheit):
    return (fahrenheit - 32) * 4/9

# Input suhu dalam Fahrenheit dari pengguna
fahrenheit_temperature = float(input("Masukkan suhu dalam Fahrenheit: "))

# Memanggil fungsi untuk konversi suhu
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
kelvin_temperature = fahrenheit_to_kelvin(fahrenheit_temperature)
reamur_temperature = fahrenheit_to_reamur(fahrenheit_temperature)

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")
print(f"Suhu dalam Reamur: {reamur_temperature} °Re")




#Tidak terstruktur
# Input suhu dalam Fahrenheit dari pengguna
fahrenheit_temperature = float(input("Masukkan suhu dalam Fahrenheit: "))

# Konversi suhu ke Celsius
celsius_temperature = (fahrenheit_temperature - 32) * 5/9

# Konversi suhu ke Kelvin
kelvin_temperature = (fahrenheit_temperature - 32) * 5/9 + 273.15

# Konversi suhu ke Reamur
reamur_temperature = (fahrenheit_temperature - 32) * 4/9

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")
print(f"Suhu dalam Reamur: {reamur_temperature} °Re")


#OOPFahrenheit
class Fahrenheit:
    def __init__(self, fahrenheit_temperature):
        self.fahrenheit_suhu = fahrenheit_temperature

    def fahrenheit_to_celsius(self):
        return (self.fahrenheit_suhu - 32) * 5/9

    def fahrenheit_to_kelvin(self):
        return (self.fahrenheit_suhu - 32) * 5/9 + 273.15

    def fahrenheit_to_reamur(self):
        return (self.fahrenheit_suhu - 32) * 4/9

# Input suhu dalam Fahrenheit dari pengguna
fahrenheit_temperature = float(input("Masukkan suhu dalam Fahrenheit: "))

# Membuat objek dari kelas Fahrenheit
converter = Fahrenheit(fahrenheit_temperature)

# Memanggil metode untuk konversi suhu
celsius_temperature = converter.fahrenheit_to_celsius()
kelvin_temperature = converter.fahrenheit_to_kelvin()
reamur_temperature = converter.fahrenheit_to_reamur()

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")
print(f"Suhu dalam Reamur: {reamur_temperature} °Re")



