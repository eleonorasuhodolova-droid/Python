from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S24", "+79234567890"),
    Smartphone("Xiaomi", "Mi 13", "+79345678901"),
    Smartphone("Google", "Pixel 8", "+79456789012"),
    Smartphone("OnePlus", "11", "+79567890123")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
