# Task 1: Functions to return first name, last name, and full name

def get_first_name(first_name):
    """
    Returns the first name provided.

    Parameters:
    first_name (str): The first name of a person.

    Returns:
    str: The first name.
    """
    return first_name

def get_last_name(last_name):
    """
    Returns the last name provided.

    Parameters:
    last_name (str): The last name of a person.

    Returns:
    str: The last name.
    """
    return last_name

def full_name(first_name, last_name):
    """
    Concatenates first name and last name into a full name.

    Parameters:
    first_name (str): The first name of a person.
    last_name (str): The last name of a person.

    Returns:
    str: A readable message displaying the full name.
    """
    return f"My full name is {get_first_name(first_name)} {get_last_name(last_name)}"

#for example:
first_name = "rofiat"
last_name = "abdulkareem"
print(full_name(first_name, last_name))


# Task 2: Transforming attribute names to follow naming conventions

details = ["first name", "last_name", "date of birth"]

def transform_attributes(details):
    """
    Transforms attribute names by replacing spaces with underscores.

    Parameters:
    details (list): A list of attribute names.

    Returns:
    list: Transformed attribute names with underscore naming conventions.
    """
    newly_transformed = [item.replace(" ", "_") for item in details]
    return newly_transformed

# for example
print(transform_attributes(details))


# Task 3: Extracting and modifying names based on specific conditions

names = ["Mayowa", "chizoba", "Chigozie"]

def filter_and_modify_names(names):
    """
    Filters names that start with a capital letter and end with 'a'.
    If a name starts with a capital letter but does not end with 'a',
    the last letter is replaced with 'a'.

    Parameters:
    names (list): A list of names.

    Returns:
    list: A list of modified and filtered names.
    """
    final_list = []
    for item in names:
        if item[0].isupper() and item.endswith("a"):
            final_list.append(item)
        elif item[0].isupper() and not item.endswith("a"):
            final_list.append(item[:-1] + "a")
    return final_list

# for example
print(filter_and_modify_names(names))


# Task 4: Checking for invalid names containing numbers

names = ["Wofai", "Zainab", "A4atullah"]

def check_code(names):
    """
    Checks if names contain only alphabetic characters.

    Parameters:
    names (list): A list of names.

    Returns:
    str: A message indicating invalid names.
    """
    invalid_name = []
    for name in names:
        if not name.isalpha():
            invalid_name.append(name)
    return f"{invalid_name}: This name contains a number or invalid characters, kindly check and rectify."

print(check_code(names))