# Write something to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file to demonstrate seek().")

# Now read using seek()
with open("example.txt", "r") as file:
    print("Reading full content:")
    print(file.read())  # Reads all content and moves pointer to the end

    # Move file pointer to beginning
    file.seek(0)
    print("\nAfter seek(0):")
    print(file.read(5))  # Reads first 5 characters: Hello

    # Move pointer to position 18 (character "f" in "file")
    file.seek(18)
    print("\nAfter seek(18):")
    print(file.read(4))  # Reads "file"

    # Move to end of the file
    file.seek(0, 2)  # 0 bytes from end (mode 2 = end of file)
    print("\nAfter seek(0, 2):")
    print("Pointer is at the end of file.")
