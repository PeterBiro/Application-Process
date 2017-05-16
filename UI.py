def get_max_col_width(table, headers):
    """
    Seeks for the longest column width.
    Args:
        @table: list of lists
        @headers: list of strings for the header to the table
    Return:
        List of integers with the column widths
    """
    col_width = [len(title) for title in headers]
    for row in table:
        for i in range(len(row)):
            if len(row[i]) > col_width[i]:
                col_width[i] = len(row[i])
    col_width = [x + 2 for x in col_width]  # for 1 char margin inside in cells
    return col_width


def show_table(table, headers):
    """
    Print a table.
    Args:
        @table: list of lists
        @headers: list of strings for the header to the table
    """
    col_width = get_max_col_width(table, headers)
    sep_line = "-" * (sum(col_width) + len(col_width) + 1)
    print(sep_line)
    for i, title in enumerate(headers):
        print("|{:^{}}".format(title.upper(), col_width[i]), end="")
    print("|")
    print(sep_line)
    for row in table:
        for i, value in enumerate(row):
            print("|{:^{}}".format(value, col_width[i]), end="")
        print("|")
        print(sep_line)


def handle_menu(menu_items):
    """
    Show a menu with options, ans ask for choice.
    Args:
        @menu_items: list of strings
    Return:
        @choice: string
    """
    for number, option in enumerate(menu_items, start=1):
        print("{} - {}".format(number, option))
    print()
    print("0 - EXIT")
    print("-"*12)
    choice = input("Your choice:")
    return choice


def main():
    headers = ["ID", "First Name", "Last Name", "Height"]
    table = [["1", "John", "Smith", "183"], ["2", "Jane", "Doe", "172"]]
    # show_table(table, headers)
    handle_menu(headers)


if __name__ == '__main__':
    main()