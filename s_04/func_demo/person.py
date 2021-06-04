def build_person(first_name, last_name, age=None):
    person = {'fisrt':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=5)
print(musician)
