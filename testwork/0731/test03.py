str_data="If you want to change your fate I think you must come to the dark horse to learn java"
words=str_data.split(" ")
print(words)
for word in words:
    if words.count(word)>=1:
        count=words.count(word)
        print(f"{word}:{count}次")






