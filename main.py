import random
import argparse


if __name__ == '__main__':

    # Set Constants
    default_length = 32
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:,./?"

    # Allocate globals
    password = ""
    character_list = ""

    # Assemble the arguments
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "-l",
        "--length",
        required=False,
        default=str(default_length),
        help="Length of password to generate. Default is 32 characters."
    )

    argument_parser.add_argument(
        "-a",
        "--alphabet",
        required=False,
        default=False,
        action="store_true",
        help="Include the alphabet in the generated password."
    )

    argument_parser.add_argument(
        "-d",
        "--digits",
        required=False,
        default=False,
        action="store_true",
        help="Include digits in the generated password."
    )

    argument_parser.add_argument(
        "-s",
        "--symbols",
        required=False,
        default=False,
        action="store_true",
        help="Include symbols in the generated password."
    )

    argument_parser.add_argument(
        "-q",
        "--quantity",
        required=False,
        default="1",
        help="How many passwords to generate. Default is 1."
    )

    # Get user-defined arguments
    user_arguments = argument_parser.parse_args()

    # Compile character list
    if not user_arguments.digits and not user_arguments.symbols and not user_arguments.alphabet:
        # Sanity check
        print("You must choose at least one kind of character. Use -h to show help.")
        exit(0)
    else:
        if user_arguments.alphabet:
            character_list += letters
        if user_arguments.symbols:
            character_list += symbols
        if user_arguments.digits:
            character_list += numbers

    # Notify user
    print(f"Generating password(s) with {int(user_arguments.length)} characters.")

    # Generate password(s)
    for quantity in range(int(user_arguments.quantity)):
        # Reset password
        password = ""
        # Get random characters
        for character in range(int(user_arguments.length)):
            password += random.choice(character_list)
        # Output password
        print(password)
