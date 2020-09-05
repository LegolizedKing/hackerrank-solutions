def minion_game(string):
    # your code goes here
    vowels="aeiouAEIOU"
    k=0
    s=0
    for i in range(len(string)):
        if string[i] in vowels:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if k==s:
        print("Draw")
    elif k>s:
        print("Kevin",k)
    else:
        print("Stuart",s)
if __name__ == '__main__':
    s = input()
    minion_game(s)x
