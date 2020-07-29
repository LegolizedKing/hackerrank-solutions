def split_and_join(line):
    # write your code here
    l=line.split(" ")
    a='-'.join(l)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
