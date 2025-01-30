continents = "France is in {} and China is in{}".format("Europe","Asia")
print(continents)


square = "{0} times {0} equals {1}".format(3,9)
#3 times 3 equals 9
print(square)


population = "{name}'s population is {pop} million".format(name="Brazil",pop=209)
print(population)

two_decimal_places = "I own {:.2f}% of the company".format(5566789)
print(two_decimal_places)

india_pop = "The apprex pop of {} is {:,}".format("india",12546758)
print(india_pop)



balance_string = "Your bank balance is ${:,.2f}".format(152354.567)

print(balance_string)