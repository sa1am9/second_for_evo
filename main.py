import random as rd
import time


def search(lst: list, name: str) -> list:
    phone_numbers = []  # list of numbers satisfying the condition

    for i in lst:
        if i.startswith(name):
            # search of the first number with input parameters
            phone_numbers.append(i)
            break

    if len(phone_numbers):
        # checking for at least one number
        try:
            for k in range(lst.index(i)+1, lst.index(i)+10):
                # as the list is sorted we check some 10 numbers on the condition
                if not lst[k].startswith(name):
                    return phone_numbers
                else:
                    phone_numbers.append(lst[k])
            return phone_numbers
        except IndexError:  # if the required numbers are at the end of the list
            return phone_numbers

    else:
        return []


if __name__ == "__main__":
    rt = time.time()
    lst = []  # list to generate numbers
    while len(lst) < 10**4:  # generation of random numbers
        q = rd.randrange(38e+9, 381e+8)
        if q not in lst:  # to not be the same
            lst.append(str(q))

    print("Time to generate a list - ", time.time()-rt)

    rt = time.time()
    lst = sorted(lst)
    print("Time to sort - ", time.time()-rt)

    rt = time.time()
    print("Sought numbers:")
    number = input("input search - ")
    print(search(lst, number))
    print("Time to search - ",time.time()-rt)
