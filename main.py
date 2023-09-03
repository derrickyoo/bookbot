print("--- Begin report of books/frankenstein.txt ---")

def character_count(words):
    results = {}
    for word in words:
        for char in word:
            key = char.lower()
            if key.isalpha():
                results[key] = results.get(key, 0) + 1
    
    return results

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)} words found in the document")
    print("")

    results = character_count(words)


    for char in results:
        print(f"The '{char}' character was found {results[char]} times")
    
