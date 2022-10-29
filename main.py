from Alogrithim import Algorithim
import random, time, threading
bins = []
numbers = [1,2,3,4,5,6,7,8,9]
file = open('bins.txt', 'r+')
data = file.readlines()
for bin in data:
    bins.append(bin)
file.close()
def main():
    cc_number = ""
    bin = random.choice(bins)
    cc_number += bin
    for i in range(10):
        l = str(random.choice(numbers))
        cc_number += l
    
    result = Algorithim.Luhn(cc_number)
    if result == True:
        print(f"[+]: Valid Credit Card Number ({cc_number})")
        with open("valid.txt", 'a+') as f:
            f.write(f"{cc_number}\n")
    else:
        print(f"[-]: Invalid Credit Card Number ({cc_number})")
    time.sleep(random.uniform(0.1, 0.2))
    return main()

if __name__ == "__main__":
    for i in range(int(input("Enter amount of threads: "))):
        threading.Thread(target=main).start()
