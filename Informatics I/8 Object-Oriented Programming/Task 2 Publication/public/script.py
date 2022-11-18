#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    # Return the local authors variable
    # Watch out that you copy the list, because else you would just pass the pointer
    # with which the variable can be changed outside the object
    def get_authors(self):
        copy = []
        for i in self.__authors:
            copy.append(i)
        return copy

    # Return the local title variable
    def get_title(self):
        return self.__title

    # Return the local year variable
    def get_year(self):
        return self.__year

    # Represent this object when calling print(str(obj)) (informal representation)
    def __str__(self):
        representation = f"Publication({str(self.__authors)}, \"{self.__title}\", {self.__year})"
        return representation.replace("'", "\"")

    # Represent this object when calling print(repr(obj))
    def __repr__(self):
        representation = f"Publication({str(self.__authors)}, \"{self.__title}\", {self.__year})"
        return representation.replace("'", "\"")

    # Calculate a hash of the Instantiated object (can be compared to verify that two objects contain the same content)
    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    # Comparison operators: '=='
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return True if sorted(other.get_authors()) == sorted(self.__authors) and other.get_title() == self.__title and other.get_year() == self.__year else False
        else: return NotImplemented

    # Comparison operators: '!='
    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return False if sorted(other.get_authors()) == sorted(self.__authors) and other.get_title() == self.__title and other.get_year() == self.__year else True
        else: return NotImplemented

    # Comparison operators: '>'
    def __lt__(self,other):
        if isinstance(self, other.__class__):
            # Compare authors
            if sorted(self.__authors) == sorted(other.get_authors()):
                # If authors are identical, compare the titles
                if self.__title == other.get_title():
                    # If titles are identical, compare the years
                    return self.__year > other.get_year()
                else: return self.__title > other.get_title()
            else: return sorted(self.__authors) > sorted(other.get_authors())
        else: return NotImplemented
        
    # Comparison operators: '>='
    def __le__(self,other):
        if isinstance(self, other.__class__):
            # Compare authors
            if sorted(self.__authors) == sorted(other.get_authors()):
                # If authors are identical, compare the titles
                if self.__title == other.get_title():
                    # If titles are identical, compare the years
                    return self.__year >= other.get_year()
                else: return self.__title >= other.get_title()
            else: return sorted(self.__authors) >= sorted(other.get_authors())
        else: return NotImplemented

    # Comparison operators: '<'
    def __lt__(self,other):
        if isinstance(self, other.__class__):
            # Compare authors
            if sorted(self.__authors) == sorted(other.get_authors()):
                # If authors are identical, compare the titles
                if self.__title == other.get_title():
                    # If titles are identical, compare the years
                    return self.__year < other.get_year()
                else: return self.__title < other.get_title()
            else: return sorted(self.__authors) < sorted(other.get_authors())
        else: return NotImplemented

    # Comparison operators: '<='
    def __le__(self,other):
        if isinstance(self, other.__class__):
            # Compare authors
            if sorted(self.__authors) == sorted(other.get_authors()):
                # If authors are identical, compare the titles
                if self.__title == other.get_title():
                    # If titles are identical, compare the years
                    return self.__year <= other.get_year()
                else: return self.__title <= other.get_title()
            else: return sorted(self.__authors) <= sorted(other.get_authors())
        else: return NotImplemented

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }