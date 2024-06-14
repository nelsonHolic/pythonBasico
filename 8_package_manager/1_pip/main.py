from camelcase import CamelCase
import django

if __name__ == "__main__":
    c = CamelCase()
    s = 'this is a sentence that needs CamelCasing!'
    print(c.hump(s))
    # This is a Sentence That Needs CamelCasing!