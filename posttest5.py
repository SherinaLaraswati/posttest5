def makananArashCafe():
    print("------------- MENU MAKANAN ARASH CAFE -------------")
menu_makanan = {
    "makanan1" : "Kentang + chicken: Rp 20.000",
    "makanan2" : "Nasi + ayam penyet: Rp 16.000",
    "makanan3" : "Mie goreng spesial: Rp 15.000",
    "makanan4" : "Seblak: Rp 15.000",
    "makanan5" : "Onion ring: Rp 15.000"   
}
def minumanArashCafe():
    print("------------- MENU MAKANAN ARASH CAFE -------------")
menu_minuman = {
    "minuman1": "chocolate: Rp 10.000",
    "minuman2": "air mineral: RP 5.000",
    "minuman3": "es kopi susu: Rp 11.000", 
    "minuman4": "americano: Rp 14.000",
    "minuman5": "green tea: Rp 13.000"  
}
makananArashCafe()
for key in menu_makanan:
    print(menu_makanan[key])
minumanArashCafe()
for key in menu_minuman:
    print(menu_minuman[key])
