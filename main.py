import csv
import os
import re

def get_tel_book():
  with open("phonebook_raw.csv", encoding='utf-8-sig') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    tel_book = []
    for row in contacts_list[1:]:
      string = ' '.join(row[0:3])
      fio = string.split()
      row = fio + row[3:7]
      if len(row) != 7:
        row.insert(5, '')
      for i in tel_book:
        if i[0:2] == row[0:2]:
          for j in range(len(i)):
            if i[j] == '' and row[j] != '':
              a = row.pop(j)
              row.append('')
              i.pop(j)
              i.insert(j, a)
            elif j == 5:
              pattern = r"(\+7|8)\s*\(?(\d{3})\)?(\s|-?)(\d{3})(\s|-?)(\d{2})(\s|-?)(\d{2})(\s?)\(?(\w{,3}\.?)\s?(\d{,4})\)?"
              substitution = r"+7(\2)\4-\6-\8\9\10\11"
              tel_n = re.sub(pattern, substitution, i[5])
              i.remove(i[j])
              i.insert(j, tel_n)
          break
      else:
        tel = row[5]
        pattern = r"(\+7|8)\s*\(?(\d{3})\)?(\s|-?)(\d{3})(\s|-?)(\d{2})(\s|-?)(\d{2})(\s?)\(?(\w{,3}\.?)\s?(\d{,4})\)?"
        substitution = r"+7(\2)\4-\6-\8\9\10\11"
        new_tel = re.sub(pattern, substitution, row[5])
        row.remove(tel)
        row.insert(5, new_tel)
        tel_book.append(row)
    else:
      tel_book.insert(0, contacts_list[0])
  return tel_book

if __name__ == '__main__':
  with open("phonebook.csv", "w", encoding='utf-8-sig') as f:
    datawriter = csv.writer(f, delimiter=';', lineterminator='\r')
    datawriter.writerows(get_tel_book())
    print(f"""В телефонной книге 'phonebook.csv' - {len(get_tel_book())} записей.
Путь к книге - {os.path.join(os.getcwd(),'phonebook.csv')}""")



