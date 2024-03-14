from contextlib import contextmanager


@contextmanager
def file_opener(file_name: str, mode: str = "r"):
    """
    Context manager for opening files.

    Args:
        file_name (str): The path to the file to be opened.
        mode (str, optional): The mode in which the file should be opened. Default is 'r'
            (read mode).

    Yields:
        file: The file object opened in the specified mode.
    """
    file = open(file_name, mode)
    try:
        yield file
    finally:
        file.close()


def main(file_name: str, mode: str = "r") -> None:
    """
    Main function to read and print the content of a file.

    Args:
        file_name (str): The path to the file to be opened.
        mode (str, optional): The mode in which the file should be opened. Default is 'r'
            (read mode).
    """
    with file_opener(file_name, mode) as file:
        content = file.read()
    print(content)


if __name__ == "__main__":
    main("test.txt")


