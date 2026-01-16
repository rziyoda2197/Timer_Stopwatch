import time


def stopwatch():
    print("Stopwatch boshlandi (to‘xtatish uchun Enter bosing)")
    start = time.time()
    input()
    end = time.time()
    print(f"O‘tgan vaqt: {round(end - start, 2)} soniya")


def timer():
    seconds = input("Necha soniya?: ")

    if not seconds.isdigit():
        print("Son kiriting")
        return

    seconds = int(seconds)

    while seconds > 0:
        print(f"Qolgan vaqt: {seconds} s", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\n Vaqt tugadi!")


def main():
    while True:
        print("\n1. Stopwatch\n2. Timer\n0. Exit")
        choice = input("Tanlang: ")

        if choice == '1': stopwatch()
        elif choice == '2': timer()
        elif choice == '0': break


if __name__ == '__main__':
    main()
