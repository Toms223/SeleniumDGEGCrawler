from json import dump

if __name__ == "__main__":
    file = open("Postos.csv", "r", encoding="utf-8")
    lines = file.read().split("\n")
    cells = []
    for line in lines:
        cells.append(line.split(";"))
    values = {}
    for i in range(0, len(cells[0]) - 1):
        values[cells[0][i]] = cells[1][i]
    file.close()
    for value in values:
        values[value] = values[value].replace("\"", "")
    with open("postos.json", "w") as file:
        dump(values, file, indent=4, )
