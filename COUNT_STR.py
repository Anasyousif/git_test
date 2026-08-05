def count_substring(string, sub_string):
    count = 0
    n = len(string)
    k = len(sub_string)
    
    # Loop from 0 to the last possible starting position
    # We use n - k + 1 to ensure the window doesn't go "off the edge"
    for i in range(0, n - k + 1):
        
        # Slice the string from current index 'i' to 'i + k'
        # This is our "window"
        if string[i : i + k] == sub_string:
            count += 1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)