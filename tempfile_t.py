import tempfile
import os

def main():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        print("Temporary file created:", temp_file.name)
        temp_file.write(b"Hello, world!\n")
        temp_file.flush()

        # Get the file descriptor of the temporary file
        fd = temp_file.fileno()
        print("File descriptor:", fd)

        # Get the name of the temporary file
        temp_file_name = os.path.basename(temp_file.name)
        print("Temporary file name:", temp_file_name)

        # Get the suffix of the temporary file
        temp_file_suffix = os.path.splitext(temp_file_name)[1]
        print("Temporary file suffix:", temp_file_suffix)

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    print("Temporary directory created:", temp_dir)

    # Create a named temporary directory
    named_temp_dir = tempfile.mkdtemp(prefix='my_temp_dir_')
    print("Named temporary directory created:", named_temp_dir)

    # Create a temporary file in a specified directory
    temp_file_in_dir = tempfile.mkstemp(dir=temp_dir)
    print("Temporary file in directory created:", temp_file_in_dir[1])

    # Create a named temporary file in a specified directory
    named_temp_file_in_dir = tempfile.mkstemp(prefix='my_temp_file_', dir=temp_dir)
    print("Named temporary file in directory created:", named_temp_file_in_dir[1])

    # Return the absolute path of a temporary file
    abs_temp_path = tempfile.mktemp()
    print("Absolute path of temporary file:", abs_temp_path)

if __name__ == "__main__":
    main()
