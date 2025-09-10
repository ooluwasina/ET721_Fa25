"""
Oluwaferanmi Oluwasina
lab 4, dictionary and functions
Sept 10,2025
"""
print("----- Example 1 Dictionary -----")
# contact dictonary
contact = {
    "Bill" : "718-111-2222",
    "Martha": "646-000-3333",
    "peter": "212-000-1111"
}
print(contact)


#save value of specfic key
user1 = contact["Martha"]
print(f"users phone numer  = {user1}")

#add new content to the dictionary
contact["Anna"] = "646-222-3333"

print(contact)

#update via a specific file

contact["peter"] = "800-000-0000"
print(contact)

print("----- Example 2: Dictionary -----")

for i in contact:
    print(i)

for i in contact:
    print(contact[i])

for i in contact:
    print(f"{i} = {contact[i]}") 


print("----- Example 3: length of a dictionary -----")
print(f"Dictionary has {len(contact)} users")

print("----- Example 4: copy a dictionary -----")
copy_contact1 = contact.copy()
copy_contact2 = dict(contact)

print(copy_contact1)
print(copy_contact2)

print("----- Example 5: Removing a Key:value pair in a dictionary -----")
print(contact)
contact.pop("peter")
print(contact)


print("----- Example 6: Removing a Key:value pair in a dictionary -----")
print(contact)
contact.update({"lucas":"212-111-1111"})
print(contact)

print("----- Example 7: return items Key, value  in a dictionary -----")
print(f"Return items = {contact.items()}")
print(f"Return Keys = {contact.keys()}")
print(f"Return values = {contact.values()}")

print("----- Example 8: dictionary application -----")

phrase = "to be or not to be"
list_phrase = phrase.split()

word_count_dict = {}

for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
for word in word_count_dict:
    print(f" '{word}' appears {word_count_dict}'")

print("----- Exercise -----")
users = ["peterpan@yahoo.com","annie@hotmail.com","Carl@hotmail.com","martha@gmail.com","cassie@yahoo.com","Josue@hotmail.com","John@hotmail.com"]
print(users)
   
email_phrase = "yahoo gmail hotmail"
phrase_list = email_phrase.split()

email_count_dict = {}
for i in users:
    if phrase_list in users[i]:
        email_count_dict[phrase_list] += 1
    else:
        email_count_dict[phrase_list] = 1

for phrase_list in email_count_dict:
    print(f" '{phrase_list}' appears {email_count_dict}'")
