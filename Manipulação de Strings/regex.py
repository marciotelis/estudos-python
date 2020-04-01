import re

email1 = "aeafas afdasfa 1234-4321 afrrf"
email2 = "21234-5555 aaa das"
email3 = "12345-2123 asrrf 12345-5432"
email4 = "12345-4321 sgrg 123454321"

# padrao = "[0123456789][0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]"
# padrao = "[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]"
# padrao = "[0-9]{4}-[0-9]{4}"
# padrao = "[0-9]{4,5}-[0-9]{4}"  # 4 ou 5
padrao = "[0-9]{4,5}[-]*[0-9]{4}"   # desta forma o hífen pode ou não estar

retorno = re.search(padrao, email2)
print(retorno.group())

retorno2 = re.findall(padrao, email4)
print(retorno2)