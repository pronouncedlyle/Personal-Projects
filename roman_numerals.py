# PART 1: Lazy Roman numerals Given a number in today's numbers, (Arabic Numeral), return its equivalent in Roman Numerals in the lazy way. 
# Lazy Roman Numerals is where Roman Numerals are added together (9 is VIIII, 4 is IIII). Here are Roman Numerals with their Arabic Numeral counterparts:

#  I -> 1
#  V -> 5
#  X -> 10
#  L -> 50
#  C -> 100
#  D -> 500
#  M -> 1000

# function lazyRomanNumeral (number) {
# set up data structure to hold numerals and numbers
# create function that uses the data sttructure and takes an integer as a n argument
# define an empty string
# loop through dictionary,
#     if # is smaller than loc in dictionary, reduce num by dictionary value
#     add numeral to the string
def to_roman(num):
    numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    answer_string = ""
    for key in numerals:
        while num >= numerals[key]:
            num -= numerals[key]
            answer_string += key
    return answer_string
print(to_roman(944))

# console.log(lazyRomanNumeral(3));

# PART 2 If a smaller number appears before a larger number, you must subtract the smaller one. Here's a list for you:

#  IV -> 4
#  IX -> 9
#  XIV -> 14
#  XLIV -> 44
#  CMXLIV -> 944
#  Sample output:
# (4) # 'IV'
# to_roman(944) # 'CMXLIV'
# to_roman(150) # CL