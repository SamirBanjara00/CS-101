# A comparable data type that represents a country by its name, capital, and population.

import stdarray
import stdio


class Country:
    # Constructs a country given its name, capital, and population.
    def __init__(self, name, capital, population):
        self.name = name  # name
        self.capital = capital  # capital city
        self.population = population  # population

    # Returns True if this country is less than the other country by name, and False otherwise.
    def __lt__(self, other):
        return self.name < other.name

    # Returns True if this and the other country have the same name, and False otherwise.
    def __eq__(self, other):
        return self.name == other.name

    # Returns a string representation of this country.
    def __str__(self):
        return self.name + ' (' + self.capital + '): ' + str(self.population)


# Unit tests the data type.
def _main():
    countries = stdarray.create1D(5, None)
    countries[0] = Country('United States', 'Washington, D.C.', 329334246)
    countries[1] = Country('Pakistan', 'Islamabad', 218719520)
    countries[2] = Country('India', 'New Delhi', 1358989650)
    countries[3] = Country('China', 'Beijing', 1401463880)
    countries[4] = Country('Indonesia', 'Jakarta', 266911900)
    stdio.writeln('Unsorted:')
    for country in countries:
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln('Sorted by name:')
    for country in sorted(countries):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln('Sorted by capital:')
    for country in sorted(countries, key=lambda x: x.capital):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln('Sorted by population:')
    for country in sorted(countries, key=lambda x: x.population):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln('Reverse sorted by population:')
    for country in sorted(countries, key=lambda x: x.population, reverse=True):
        stdio.writeln(country)


if __name__ == '__main__':
    _main()
