def main():
    string = input()
    result = 0;
    for i in range(len(string)):
        result += (ord(string[i]) - 64) * 26 ** (len(string) - i - 1)
    print(result)

main()