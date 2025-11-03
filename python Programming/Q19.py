print("Om Nimmalwar")
import itertools

lst = [1, 2, 3, 4]
two = list(itertools.combinations(lst, 2))
three = list(itertools.combinations(lst, 3))
result = {'Two_Digit': two, 'Three_Digit': three}
print(result)
