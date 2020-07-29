def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            d=True
            for j in range(len(sub_string)):
                if i+j>=len(string):
                    d=False
                if i+j<len(string) and string[i+j]!=sub_string[j]:
                    d=False
            if d:
                count+=1
                
                
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
