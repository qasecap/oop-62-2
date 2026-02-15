data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for item in data:
    if item.isdigit():  # Если это строка из цифр
        codes.append(item)
    else:
        designations.append(item)

operators = {}
for i in range(len(designations)):
    operators[designations[i]] = {codes[i]}

operators.pop("Katel")
operators.pop("Fonex")

operators["O!"].add("0700")
operators["O!"].add("0500")

operators["Megacom"].add("0999")
operators["Megacom"].add("0555")

operators["Beeline"].add("0222")
operators["Beeline"].add("0777")

for name, code_set in operators.items():
    print(f"{name} - {code_set}")