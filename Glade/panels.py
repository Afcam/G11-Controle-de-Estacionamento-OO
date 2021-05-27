#!/usr/bin/env python3

import os
from simple_term_menu import TerminalMenu


def main():
    fruits = ["[a] apple", "[b] banana", "[o] orange"]
    terminal_menu = TerminalMenu(fruits, title="Fruits")
    menu_entry_index = terminal_menu.show()
    print(menu_entry_index)


if __name__ == "__main__":
    main()