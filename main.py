from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8-sig') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  tel_book = []
  for row in contacts_list[1:]:
    new_tel_book = []
    string = ' '.join(row[0:3])
    fio = string.split()
    row = fio + row[3:]
    for i in tel_book:
      if i[0:2] == row[0:2]:
        for j in range(len(i)):
          if i[j] == '':
            i.insert(j, row[j])
          elif row[j] == '':
            row.insert(j, i[j])
          i[j] = row[j]
        break
      new_tel_book.append(i)
    tel_book.append(row)
print(tel_book)

  pattern = r"(\+7|8)\s*\(?(\d{3})\)?(\s|-?)(\d{3})(\s|-?)(\d{2})(\s|-?)(\d{2})(\s?)\(?(\w{,3}\.?)\s?(\d{,4})\)?"
  substitution = r"+7(\2)\4-\6-\8\9\10\11"
  a = re.sub(pattern, substitution, row[5])
  print(row)


with open("phonebook.csv", "w", encoding='utf-8-sig') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(l)



