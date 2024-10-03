# Wersja 1:
# Pliki są importowane z dump folderów (niezależnie od ich nazwy) - DONE
# Pliki są poprawnie importowane do klasy - DONE
# zamienić for loop na list comprehension - do zrobienia
# Teraz trzeba stworzyć logikę, która będzie porównywać ze sobą oba raporty - ZADANIE NA DZIŚ:
# - 
# Na razie niech raporty będą identyczne - chcemy tylko uzyskać logikę do porównywania ich ze sobą
# Na pewno stworzyć klasę (na razie "na sztywno")
# Potem stworzyć listy słowników przechowujące dane
# Dalej stworzyć logikę, która porównuje ze sobą instancje klas i jakoś zapisuje to do jeszcze innej zmiennej którą można wydrukować

# Raport jest printowany (w kolejnej wersji będzie zapisywany do ładniejszego pliku)
# Na tym etapie chcemy mieć tylko zestawienie transakcji zgodnych i niezgodnych ze sobą
# - dalsza logika w kolejnych wersjach
# Użytkownik określa treshold w inpucie

import csv
import datetime
import glob


DUMP_BROKER = glob.glob(r'dump_broker\*')
DUMP_SYSTEM = glob.glob(r'dump_system\*')
DATE_FORMAT = '%d.%m.%Y'

class Transaction:
    def __init__(self, date, description, security_name, security_id, qty, dr, cr):
        self.date = date
        self.description = description
        self.security_name = security_name
        self.security_id = security_id
        self.qty = qty
        self.dr = dr
        self.cr = cr
    
    def __str__(self):
        return f"Transaction(date='{self.date.date()}', description='{self.description}', security_name='{self.security_name}', security_id='{self.security_id}', qty='{self.qty}', dr='{self.dr}', cr='{self.cr}'"
    
    def __repr__(self):
        return f"Date:'{self.date.date()}', Description:'{self.description}', Security_name:'{self.security_name}', Security_ID:'{self.security_id}', QTY:'{self.qty}', DR:'{self.dr}', CR:'{self.cr}'"
        

def csv_reader(filepath):
    with open(filepath, mode='r', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        reader_list = list(reader)
    return reader_list

# def create_TransactionItem_from_dict(file):
#     transactions = []
#     for row in file:
#         transactions.append(Transaction(
#             date=datetime.datetime.strptime((row['Date']), DATE_FORMAT),
#             description=row['Description'],
#             security_name=row['Security_name'],
#             security_id=row['Security_ID'],
#             qty=row['QTY'],
#             dr=row['DR'],
#             cr=row['CR'],
#         ))
#     return transactions


def print_by_class(instances):
    for line in instances:
        print(repr(line))
        # print(line)
        # print(type(line.date))


def main():
    broker_file = csv_reader(DUMP_BROKER[0])
    system_file = csv_reader(DUMP_SYSTEM[0])

    # broker_read_class = create_TransactionItem_from_dict(broker_file)
    broker_read_class = [Transaction(datetime.datetime.strptime((row['Date']), DATE_FORMAT), row['Description'], row['Security_name'], row['Security_ID'], row['QTY'], row['DR'], row['CR']) for row in broker_file]

    system_read_class = [Transaction(datetime.datetime.strptime((row['Date']), DATE_FORMAT), row['Description'], row['Security_name'], row['Security_ID'], row['QTY'], row['DR'], row['CR']) for row in system_file]

    print_by_class(broker_read_class)
    print_by_class(system_read_class)


if __name__ == '__main__':
    main()