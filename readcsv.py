import csv

csv_file = open("./test_stock.csv", "r", encoding="utf-8", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    print(row[1])