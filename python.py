def create_playfair_matrix(key):
    """
    Creates a 5x5 Playfair cipher matrix using the provided key.

    Args:
    - key (str): The keyword for the cipher.

    Returns:
    - list: A 5x5 matrix (list of lists).
    """
    # Prepare the key by removing duplicates and excluding 'J'
    key = key.upper().replace("J", "I")
    matrix_key = "".join(dict.fromkeys(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))

    # Build the 5x5 matrix
    matrix = [list(matrix_key[i:i+5]) for i in range(0, 25, 5)]
    return matrix


def prepare_text(text):
    """
    Prepares plaintext for Playfair cipher encryption.

    Args:
    - text (str): The plaintext.

    Returns:
    - str: Prepared text as digraphs.
    """
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))  # Remove non-alphabetic characters
    prepared_text = ""

    i = 0
    while i < len(text):
        prepared_text += text[i]

        # Check for pairs
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text += "X"
        elif i + 1 < len(text):
            prepared_text += text[i + 1]
            i += 1
        else:
            # Add padding if needed
            prepared_text += "X"

        i += 1

    return prepared_text


def find_position(matrix, letter):
    """
    Finds the row and column of a letter in the Playfair matrix.

    Args:
    - matrix (list): The Playfair matrix.
    - letter (str): The letter to find.

    Returns:
    - tuple: Row and column indices of the letter.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None


def encrypt_playfair(plaintext, key):
    """
    Encrypts plaintext using the Playfair cipher.

    Args:
    - plaintext (str): The text to encrypt.
    - key (str): The keyword for the cipher.

    Returns:
    - str: Encrypted ciphertext.
    """
    matrix = create_playfair_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        letter1, letter2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, letter1)
        row2, col2 = find_position(matrix, letter2)

        # Same row
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        # Same column
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        # Rectangle
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


# Example Usage
if __name__ == "__main__":
    # Input the keyword and plaintext
    key = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")

    # Encrypt the plaintext
    ciphertext = encrypt_playfair(plaintext, key)
    print("Encrypted Text:", ciphertext)