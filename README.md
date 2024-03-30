# Playfair-Cipher

## Overview

The Playfair Cipher project is a web-based application designed to demonstrate the encryption and decryption processes of the Playfair cipher algorithm interactively. Developed using Flask, a popular Python web framework, this application allows users to input plaintext for encryption or ciphertext for decryption along with a key. The application then visually presents each step of the encryption or decryption process, offering a hands-on learning experience about the Playfair cipher's inner workings.

## Features

- **Interactive Encryption/Decryption**: Users can enter either plaintext for encryption or ciphertext for decryption along with a custom key.
- **Step-by-Step Visualization**: The application breaks down the encryption or decryption process into steps, visually demonstrating how the Playfair cipher operates.
- **Custom Key Support**: Users can define their own keys for the cipher, adding an extra layer of personalization to the encryption/decryption process.

## How Playfair Cipher Works

The Playfair cipher is a digraph substitution cipher that encrypts/decrypts pairs of letters (digraphs), unlike traditional ciphers, which do so letter by letter. This method makes it significantly harder to crack. Here's a simplified overview of its operation:

### Encryption

1. **Key Matrix Creation**: A 5x5 matrix is generated from a keyword, with repeated letters omitted. The rest of the alphabet fills the remaining spaces (I/J are usually combined).
2. **Preparation**: The plaintext is divided into digraphs (pairs of letters). If a pair contains the same letter, a filler letter ('X') is inserted.
3. **Encryption Rules**:
   - If both letters are in the same row, each letter is replaced by the one immediately to its right (wrap around to the start of the row if needed).
   - If both letters are in the same column, each letter is replaced by the one immediately below it (wrap around to the top if necessary).
   - If the letters form a rectangle, each letter is replaced by the letter on the same row but in the opposite corner of the rectangle.

### Decryption

Decryption follows the reverse process of encryption, using the same key:

- For the same row or column, move to the left or up, respectively.
- For the rectangle rule, the reverse substitution is applied.

## Usage
- To encrypt, enter the plaintext and a key, select "Encryption", and click "GO".
- To decrypt, enter the ciphertext and a key, select "Decryption", and click "GO".
- The result page will display the step-by-step encryption or decryption process, along with the resulting text and the key matrix used.
