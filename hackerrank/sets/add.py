n = int(input())
countries = []
for i in range(n):
    country = str(input())
    if country not in countries:
        countries.append(country)
print(len(countries))