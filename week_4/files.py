def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (adds "Modified: " to each line),
    and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = "Modified: " + line
                outfile.write(modified_line)
        print(f"File '{input_filename}' successfully modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Gets the input and output filenames from the user and calls the file modification function.
    """
    while True:
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")

        if not input_filename or not output_filename:
            print("Filenames cannot be empty. Please try again.")
            continue
        break

    modify_and_write_file(input_filename, output_filename)

if __name__ == "__main__":
    main()