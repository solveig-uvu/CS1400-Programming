def interleave(odds:list, evens:list) -> list:
    # Using a for loop to iterate up to the maximum lengths of the two lists.
    interleavedList = []
    for num in range(max(len(odds), len(evens))):
        if num < len(odds):
            interleavedList.append(odds[num])
        if num < len(evens):
            interleavedList.append(evens[num])
    return interleavedList

def main():
    odds = [11, 33, 55]
    evens = [22, 44, 66, 88]
    result = interleave(odds, evens)
    print("Interleaved list: ", result)

if __name__ == '__main__':
    main()