def output_result(reg: str, inp: str, result: bool) -> None:
    # print(f"Input: '{reg}|{inp}'     Output: {result}")
    print(f"{result}")


def regexp_compare(regex: str, inpt: str) -> bool:
    # Wild card regex, empty regex should always return True
    if regex == "." or regex == "":
        return True

    # Empty input returns always False if regex is not empty
    if inpt == "":
        return False

    return regex == inpt

def main():
    try:
        user_regex, user_input = input().split("|")
        if user_regex in ["", None]:
            user_regex = ""
        if user_input in ["", None]:
            user_input = ""
    except ValueError:
        print("Invalid input")
        return

    # print(f"Input: '{user_regex}|{user_input}'") # Debug

    result = regexp_compare(user_regex, user_input)
    output_result(user_regex,user_input,result)


if __name__ == "__main__":
    main()