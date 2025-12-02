
def number_checker():
    spam = int(input('Enter a number: '))
    assert spam > 10
    print("Spam is a number greater then 10")

number_checker()