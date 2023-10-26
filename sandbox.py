import pyperclip
import difflib

# Function to read the content of the text file.  The text file will be the previous clipboard data from the last run
def read_file(filename):
    with open(filename, 'r', encoding='unicode-escape') as file:
        return file.read()

# Function to compare current clipboard content with previous clipboard file content
def compare_clipboard_with_file(clipboard_content, file_content):
    d = difflib.Differ()
    diff = list(d.compare(clipboard_content.splitlines(), file_content.splitlines()))
    
    # Filter and create a list of differences that start with '- ', and strip the '- ' characters by starting on character 3
    differences = [line[2:] for line in diff if line.startswith('- ')]
    
    return '\n'.join(differences)

# Function to write differences to a text file
def write_clipboard_to_file(clipboard, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(clipboard)

def main():
    # Specify the path to the previous clipboard text file
    file_path = 'C:/Users/Willi/OneDrive - advancediscovery/Projects/Python/Adio - Repo/adio-cc-wl002adio01-adio-general-001-repo/Adio - Clipboard/PreviousClipboard.txt'

    # Capture the current clipboard content
    clipboard_content = pyperclip.paste()

    # Read the content of the text file
    file_content = read_file(file_path)

    # Compare clipboard content with file content
    differences = compare_clipboard_with_file(clipboard_content, file_content)

    # Write over the previous clipboard text file with differences
    write_clipboard_to_file(clipboard_content, file_path)

    # Copy the differences back into the clipboard
    pyperclip.copy(differences)

if __name__ == '__main__':
    main()
