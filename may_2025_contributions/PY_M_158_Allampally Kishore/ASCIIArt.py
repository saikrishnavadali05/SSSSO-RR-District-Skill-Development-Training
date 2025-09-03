import pyfiglet

def draw_box(size, filled=True):
    for i in range(size):
        if filled or i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

def draw_triangle(size, filled=True):
    for i in range(1, size + 1):
        if filled or i == 1 or i == size:
            print('*' * i)
        else:
            print('*' + ' ' * (i - 2) + '*')

def text_to_ascii(text):
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)

def main():
    print("Welcome to the ASCII Art Generator!")
    print("Choose an option:")
    print("1. Draw Box")
    print("2. Draw Triangle")
    print("3. Convert Text to ASCII Banner")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        size = int(input("Enter size of box: "))
        style = input("Filled or hollow? (f/h): ").lower()
        draw_box(size, filled=(style == 'f'))
    elif choice == '2':
        size = int(input("Enter size of triangle: "))
        style = input("Filled or hollow? (f/h): ").lower()
        draw_triangle(size, filled=(style == 'f'))
    elif choice == '3':
        text = input("Enter text to convert: ")
        text_to_ascii(text)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
