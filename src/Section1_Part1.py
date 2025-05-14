def accepts_string(s):
    count = 0
    for char in s:
        if char == '1':
            count += 1
        elif char != '0':
            return False 
    
    return count % 3 == 0

test_strings = [
    "",       
    "000",    
    "111",    
    "10101",  
    "1",      
    "11",     
    "11011",  
    "abc"     
]

for s in test_strings:
    result = "Accepted" if accepts_string(s) else "Rejected"
    print(f"'{s}': {result}")