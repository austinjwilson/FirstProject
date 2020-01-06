# concat_name("First", "Last")
# concat_name.reverse()
# print(concat_name)

def say_hello(greeting, species):
    print(f"{species} {greeting}!")


say_hello("Hello", "Humanoids")
say_hello("0100100001100101011011000110110001101111", "Cyborgs")
say_hello("Click Click Click", "Arachnids")


def concat_name(first, last):
    print(f"\"{last}, {first}\"")


concat_name("First", "Last")
concat_name("John", "Doe")
concat_name("Mary", "Jane")
