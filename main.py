import win32com.client
from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
def AlphabetPosition(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return int(' '.join(numbers))

path = r'Russia.xlsx';
x1 = win32com.client.DispatchEx("Excel.Application");
wb1 = x1.Workbooks.Open(path);
x1.DisplayAlerts = False;

print(x1.Cells(9, AlphabetPosition('F')).Value);
x1.Cells(9, AlphabetPosition('F')).Value = 2;
print(x1.Cells(9, AlphabetPosition('F')).Value);
print(x1.Cells(18, AlphabetPosition('H')).Value);
x1.Application.Quit();
