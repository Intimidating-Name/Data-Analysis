#!/usr/bin/env python3

def word_frequencies(filename):
    f = open(filename, mode="r")
    lines = [i[:-1].strip("""!"#$%&'()*,-./:;?@[]_""").split(" ") for i in f.readlines()]
    frequencies = {}
    for i in lines:
        for j in i:
            j = j.strip("""!"#$%&'()*,-./:;?@[]_""")
            if j in frequencies:
                frequencies[j] += 1
            else:
                frequencies[j] = 1
    f.close()
    return frequencies

def main():
    d = word_frequencies("src/alice.txt")
    print(d)


    #if d["creating"] != 3:
    #    print("Incorrect count for word 'creating'!")
    #if d["Carroll"] != 3:
    #    print("Incorrect count for word 'Carroll'!")
    #if d["sleepy"] != 2:
    #    print("Incorrect count for word 'sleepy'!")
    #if d["Rabbit"] != 28:
    #    print("Incorrect count for word 'Rabbit'!")
    #
    #if len(d) != 2424:
    #    print(f"Wrong number of words in the dictionary, should be 2424 but is {len(d)}")
    


if __name__ == "__main__":
    main()
