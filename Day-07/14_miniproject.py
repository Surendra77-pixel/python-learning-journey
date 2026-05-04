#  Dictionary Mini Project

# Dictionary to store words
dictionary = {}

while True:
    print("\n📚 --- SMART DICTIONARY ---")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Word")
    print("4. Delete Word")
    print("5. Show All Words")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1️ Add Word
    if choice == "1":
        word = input("Enter word: ")
        meaning = input("Enter meaning: ")

        if word in dictionary:
            print("⚠️ Word already exists!")
        else:
            dictionary[word] = meaning
            print("✅ Word added successfully!")

    # 2️ Search Word
    elif choice == "2":
        word = input("Enter word to search: ").lower()

        if word in dictionary:
            print(f"📖 Meaning: {dictionary[word]}")
        else:
            print("❌ Word not found!")

    # 3️ Update Word
    elif choice == "3":
        word = input("Enter word to update: ").lower()

        if word in dictionary:
            new_meaning = input("Enter new meaning: ")
            dictionary[word] = new_meaning
            print("🔄 Word updated successfully!")
        else:
            print("❌ Word not found!")

    # 4️ Delete Word
    elif choice == "4":
        word = input("Enter word to delete: ").lower()

        if word in dictionary:
            del dictionary[word]
            print("🗑️ Word deleted successfully!")
        else:
            print("❌ Word not found!")
 
    # 5️ Show All Words
    elif choice == "5":
        if len(dictionary) == 0:
            print("📭 Dictionary is empty!")
        else:
            print("\n📚 All Words:")
            for word, meaning in dictionary.items():
                print(f"{word} : {meaning}")

    # 6️ Exit
    elif choice == "6":
        print("👋 Exiting Dictionary... Bye!")
        break

    # Invalid choice
    else:
        print("⚠️ Invalid choice! Try again.")