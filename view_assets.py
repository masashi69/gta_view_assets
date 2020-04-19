import csv
import matplotlib.pyplot as plt

with open('.\\data\\gtacashflow.csv', 'r') as f:
    Assets = csv.reader(f)
    DATA = list(Assets)

x = list() 
y_cash = list()
y_bank = list()

for a in DATA:
    x.append(a[0])
    y_cash.append(int(a[1]))
    y_bank.append(int(a[2]))

# Create graph as bar, add legend
p1 = plt.bar(x, y_bank, color='blue')
p2 = plt.bar(x, y_cash, bottom=y_bank, color='green')
plt.legend((p1[0],p2[0]),('Bank','Cash'))

# Fine-tune labels
plt.title('GTA Online Asset Flow')
plt.xticks(rotation=45)
plt.ylabel('Assets ($)')

# Set the maximum y-axis limit value for bank due to large propotion
plt.ylim([0, max(y_bank) * 1.5])

plt.show()

