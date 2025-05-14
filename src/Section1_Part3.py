def simulate_tm_ww(input_str):
    tape = list(input_str)
    n = len(tape)
    
    if n == 0:
        return True
    
    if n % 2 != 0:
        return False
    
    half = n // 2
    first_half = tape[:half]
    second_half = tape[half:]
    
    for i in range(half):
        if first_half[i] != second_half[i]:
            return False
    
    return True

test_cases = [
    ("", True),      
    ("00", True),    # w=0
    ("01", False),   # Not ww
    ("0101", True),  # w=01
    ("0110", False), # Not ww
    ("0000", True),  # w=00
    ("001100", True), # w=001
    ("001101", False), # Not ww
    ("0", False),    # Odd length
    ("1", False)     # Odd length
]

print("Testing TM for L = {ww}:")
for input_str, expected in test_cases:
    result = simulate_tm_ww(input_str)
    print(f"Input: '{input_str}'\tResult: {'Accept' if result else 'Reject'}"
          f"\tExpected: {'Accept' if expected else 'Reject'}")
    assert result == expected, f"Failed for input '{input_str}'"

print("All tests passed!")