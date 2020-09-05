def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        l=string[i:i+k]
        sp=''
        for u in l:
            if u not in sp:
                sp+=u
        print(sp)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)	
