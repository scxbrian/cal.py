def main():
    try:
        # Ask user for input file
        input_filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified file saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
