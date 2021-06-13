import random
import argparse
import math

# Allocate globals
password = ""
character_list = ""
argument_parser = argparse.ArgumentParser()

# Set Constants
default_length = 32
characters_to_use = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "symbols": "!@#$%^&*()-_=+[]{};:,./?"
}


# Functions
def process_arguments(the_parser):
    # Assemble the arguments
    the_parser.add_argument(
        "-l",
        "--length",
        required=False,
        default=str(default_length),
        help="Size of password to generate. Default is 32 characters."
    )
    the_parser.add_argument(
        "-lc",
        "--lowercase",
        required=False,
        default=False,
        action="store_true",
        help="Include the alphabet in the generated password."
    )
    the_parser.add_argument(
        "-uc",
        "--uppercase",
        required=False,
        default=False,
        action="store_true",
        help="Include uppercase alphabet in the generated password."
    )
    the_parser.add_argument(
        "-d",
        "--digits",
        required=False,
        default=False,
        action="store_true",
        help="Include digits in the generated password."
    )
    the_parser.add_argument(
        "-s",
        "--symbols",
        required=False,
        default=False,
        action="store_true",
        help="Include symbols in the generated password."
    )
    the_parser.add_argument(
        "-q",
        "--quantity",
        required=False,
        default="1",
        help="How many passwords to generate. Default is 1."
    )
    return the_parser.parse_args()


def compile_characters(the_args, the_chars):
    compiled_list = ""
    # If user did not choose any options for characters to include, include them all.
    if not user_arguments.digits \
            and not the_args.symbols \
            and not the_args.uppercase \
            and not the_args.lowercase:
        compiled_list = the_chars["lowercase"] \
                         + the_chars["uppercase"] \
                         + the_chars["symbols"] \
                         + the_chars["digits"]
    else:
        if the_args.lowercase:
            compiled_list += the_chars["lowercase"]
        if the_args.uppercase:
            compiled_list += the_chars["uppercase"]
        if the_args.symbols:
            compiled_list += the_chars["symbols"]
        if the_args.digits:
            compiled_list += the_chars["digits"]

    return compiled_list


if __name__ == '__main__':
    # Get user-defined arguments
    user_arguments = process_arguments(argument_parser)

    # Compile the character list
    character_list = compile_characters(user_arguments, characters_to_use)

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
        entropy = len(password) * math.log(len(list(character_list)), 2)
        print(entropy)
