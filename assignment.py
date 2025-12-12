

# 1. Transform and Clean Data
products = ["  LAPTOP  ", "phone  ", " Tablet ", "CAMERA  "]

clean_products = list(map(lambda x: x.strip().title(), products))
print("1) Cleaned Products:", clean_products)



# 2. Convert Temperatures (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print("2) Fahrenheit:", fahrenheit)



# 3. Apply Multiple Transformations (Square then +10)
nums = [1, 2, 3, 4, 5]

transformed = list(map(lambda n: n**2 + 10, nums))
print("3) Squared + 10:", transformed)



# 4. Extract First and Last Characters
words = ["python", "Lambda", "programming", "map", "function"]

first_last = list(map(lambda w: (w[0], w[-1]), words))
print("4) First and Last Characters:", first_last)



# 5. Nested Map Transformation (Increase by 5% and round)
marks = [
    [45, 80, 70],
    [90, 60, 100],
    [88, 76, 92]
]

updated_marks = list(
    map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks)
)

print("5) Updated Marks:", updated_marks)



# 6. Normalize numbers between 0 and 1
nums2 = [0, 20, 40, 60, 80, 100]

normalized = list(map(lambda x: x / 100, nums2))
print("6) Normalized:", normalized)



# 7. Extract length of each word per sentence (nested map)
sentences = [
    ["I", "love", "Python"],
    ["map", "and", "lambda", "are", "powerful"],
]

lengths = list(
    map(lambda row: list(map(lambda w: len(w), row)), sentences)
)

print("7) Word Lengths:", lengths)

