import statistics

user = int(input("Enter a number: "))

number = []
for i in range(user):
    num = float(input(f"Enter number {i+1}: "))
    number.append(num)
print(number)

print("What do yo want to calculate?")
print("1. Mean")
print("2. Median")
print("3. Mode")

choice = input("Enter a choice to be calculate a sum: (1/2/3) : ")

if choice == '1':
    print("mean = ",statistics.mean(number))
elif choice == '2':
    print("median = ",statistics.median(number))
elif choice == '3':
    try:
        print("Mode",statistics.mode(number))
    except statistics.StatisticsError:
        print("No uniqe mode Found")
else:
    print("Invalid choice!!")