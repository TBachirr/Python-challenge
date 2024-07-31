
def format_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}".title()
    return full_name
print(format_name("janis", "joplin"))