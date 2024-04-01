# Function to check if the alphabets were correctly retrieved
def check_alphabets(word, retrieved):
    # Sort both words
    sorted_word = ''.join(sorted(word))
    sorted_retrieved = ''.join(sorted(retrieved))
    
    # If the sorted words are the same, then alphabets were retrieved correctly
    if sorted_word == sorted_retrieved:
        return "same"
    else:
        return "different"

# Input processing
cases = 1
while True:
    word = input()
    if word == 'END':
        break
    retrieved = input()
    if retrieved == 'END':
        break
    
    # Check if the alphabets were correctly retrieved
    result = check_alphabets(word, retrieved)
    
    # Output the result
    print(f"Case {cases}: {result}")
    cases += 1
