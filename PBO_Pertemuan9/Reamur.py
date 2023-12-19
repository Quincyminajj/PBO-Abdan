#Terstruktur
def reamur_to_celsius(reamur):
    return reamur * 5/4

def reamur_to_fahrenheit(reamur):
    return (reamur * 9/4) + 32

def reamur_to_kelvin(reamur):
    return (reamur * 5/4) + 273.15

# Input suhu dalam Reamur dari pengguna
reamur_temperature = float(input("Masukkan suhu dalam Reamur: "))

# Memanggil fungsi untuk konversi suhu
celsius_temperature = reamur_to_celsius(reamur_temperature)
fahrenheit_temperature = reamur_to_fahrenheit(reamur_temperature)
kelvin_temperature = reamur_to_kelvin(reamur_temperature)

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Fahrenheit: {fahrenheit_temperature} °F")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")




#TidakStruktur
# Input suhu dalam Reamur dari pengguna
reamur_temperature = float(input("Masukkan suhu dalam Reamur: "))

# Konversi suhu ke Celsius
celsius_temperature = reamur_temperature * 5/4

# Konversi suhu ke Fahrenheit
fahrenheit_temperature = (reamur_temperature * 9/4) + 32

# Konversi suhu ke Kelvin
kelvin_temperature = (reamur_temperature * 5/4) + 273.15

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Fahrenheit: {fahrenheit_temperature} °F")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")



#OOPReamur
class ReamurConverter:
    def __init__(self, reamur_temperature):
        self.reamur_temperature = reamur_temperature

    def reamur_to_celsius(self):
        return self.reamur_temperature * 5/4

    def reamur_to_fahrenheit(self):
        return (self.reamur_temperature * 9/4) + 32

    def reamur_to_kelvin(self):
        return (self.reamur_temperature * 5/4) + 273.15

# Input suhu dalam Reamur dari pengguna
reamur_temperature = float(input("Masukkan suhu dalam Reamur: "))

# Membuat objek dari kelas ReamurConverter
converter = ReamurConverter(reamur_temperature)

# Memanggil metode untuk konversi suhu
celsius_temperature = converter.reamur_to_celsius()
fahrenheit_temperature = converter.reamur_to_fahrenheit()
kelvin_temperature = converter.reamur_to_kelvin()

# Menampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius_temperature} °C")
print(f"Suhu dalam Fahrenheit: {fahrenheit_temperature} °F")
print(f"Suhu dalam Kelvin: {kelvin_temperature} K")
