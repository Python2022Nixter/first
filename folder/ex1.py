NAME = "ex1"

PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737241846027987019968"

def main():
    print("Hello, World!")
    print("PI:", PI)
print(NAME) # ex1 is the name of the file (ex1.py) срабатывает при запуске файла import
# or __name__

print(__name__) # ex1 is the name of the file (ex1.py) срабатывает при запуске файла import

if __name__ == "__main__":
    print("This is the main function")
    print("Сработал код из файла ex1.py")