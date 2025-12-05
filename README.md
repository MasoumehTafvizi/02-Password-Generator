# Password Generator - OOP Approach
This project contains a password generator application written in Python. The generator can create three types of passwords:
1. Random Passwords
2. Memorable Passwords
3. Pin Codes

# How it works
The password generator uses the Python random module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:
1. `RandomPasswordGenerator`: Generates random passwords based on specified length and character types (uppercase, lowercase, digits, special characters).
2. `MemorablePasswordGenerator`: Generates memorable passwords by combining random words from a predefined list. The NLTK English language corpus is chosen by default for word selection. It can optionally separate the words with a separator and use capitalized words.
3. `PinCodeGenerator`: Generates numeric pin codes of specified length.

Each generator class inherits from a base `PasswordGenerator` class. They each override the base class's `generate()` method in order to provide their own unique password generation functionality.

# Requirements
- Python 3.13 or higher
- NLTK library (Natural Language Toolkit)

To install NLTK, use pip:
```bash
pip install nltk
```
After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:
```python
import nltk
nltk.download('words')
```
That's all you need to know to get started with this project. Enjoy generating passwords!

# Running the Project
Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:
```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python main.py
```
Be sure to replace `/your/path/to/main/directory` with the actual path to the directory containing your project.


