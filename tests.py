from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()


from functions.get_file_content import get_file_content

print("Test 1: get_file_content('calculator', 'main.py')")
print(get_file_content("calculator", "main.py"))
print()

print("Test 2: get_file_content('calculator', 'pkg/calculator.py')")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Test 3: get_file_content('calculator', '/bin/cat')  # Should return an error")
print(get_file_content("calculator", "/bin/cat"))
print()

# Optional: create a long file and test truncation
# This assumes "lorem.txt" exists and contains more than 10000 characters
# To manually test truncation, you can create such a file for local testing

print("Test 4: get_file_content('calculator', 'lorem.txt')  # Should truncate if too long")
print(get_file_content("calculator", "lorem.txt"))
print()
