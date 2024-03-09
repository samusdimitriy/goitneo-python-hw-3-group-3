from contact_classes import Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return str(ve)
        except IndexError:
            return "Invalid command."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.phones[0]
    else:
        raise KeyError

@input_error
def show_all(book):
    if not book.data:
        return "No contacts found."
    return "\n".join([str(record) for record in book.data.values()])

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return "Birthday not set."
    else:
        raise KeyError

@input_error
def birthdays(book):
    next_week_birthdays = book.get_birthdays_per_week()
    if not next_week_birthdays:
        return "No birthdays next week."
    else:
        return "\n".join([f"{day}: {', '.join(names)}" for day, names in next_week_birthdays.items()])
