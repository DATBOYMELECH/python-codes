#Dictionary is a changeable unordered collection of unique key: value parts

rivers = {
"Adoni": "Ngo", 
"Ikwerre": "Isiokpo" ,
"Obio/Akpor": "Rumuodomaya"}
print(rivers)

Melech = { 
"Name" : "Melech Amaewhule",
"Email_Address":" Melech38@gmail.com",
"Age": 13,
"Male": True,
"Height": 60.61 
}
print(Melech["Name"])
print(Melech.keys())
print(Melech.values())
print(Melech.items())



for key, value in rivers.items():
    print(key, ":", value)

#CLASS WORK
"""""""""CREATE A DICTIONARY OF 10 COUNTRIES AND THEIR CAPITALS"""





Country = {
    "Nigeria": "Abuja",
    "Tokyo": "Japan",
    "United States of America": "WASHINGTION DC",
    "Ghana": "Accra",
    "Canada": "Ottawa",
    "Australia": "	Canberra",
}
print(Country.items())