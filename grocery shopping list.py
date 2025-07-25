print('Catatan Belanja Mingguan')

shopping = list(('Beras 2 KG','Susu UHT 1 Liter','Roti tawar 2 PCS','Galon air 15 liter'))

def shopping_list():
    shopping
    print(shopping)

shopping_list()

def updated_list():
    shopping.append('Minyak goreng 1 liter')
    print('Update List Belanjaan Mingguan!')
    print(shopping)

updated_list()