import lizard
file_list = [
    "/Users/dpradhan/Documents/phD/Apptest/Dummy_data/buggy/Main.java",
    "/Users/dpradhan/Documents/phD/Apptest/Dummy_data/fixed/Main.java"
]
for file in file_list:
    lizard_data = lizard.analyze_file(file)
    data = lizard_data.function_list[0].__dict__
    filename = data.pop("filename")
    print(filename)
    for key, value in data.items():
        print(key + ": " + str(value))
    print("\n")
