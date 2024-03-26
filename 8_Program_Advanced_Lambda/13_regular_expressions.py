import re


def match_literal_characters():
    """
    Match literal characters.
    """
    pattern = re.compile(r'hello')
    result = pattern.search('hello world')
    if result:
        print("Pattern found:", result.group())


def match_any_single_character():
    """
    Match any single character.
    """
    pattern = re.compile(r'gr.y')
    result = pattern.search('grey')
    if result:
        print("Pattern found:", result.group())


def match_beginning_of_string():
    """
    Match beginning of a string.
    """
    pattern = re.compile(r'^hello')
    result = pattern.match('hello world')
    if result:
        print("Pattern found:", result.group())


def match_end_of_string():
    """
    Match end of a string.
    """
    pattern = re.compile(r'world$')
    result = pattern.search('hello world')
    if result:
        print("Pattern found:", result.group())


def match_zero_or_more_occurrences():
    """
    Match zero or more occurrences.
    """
    pattern = re.compile(r'a*b')
    result = pattern.search('b')
    if result:
        print("Pattern found:", result.group())


def match_one_or_more_occurrences():
    """
    Match one or more occurrences.
    """
    pattern = re.compile(r'a+b')
    result = pattern.search('aaaab')
    if result:
        print("Pattern found:", result.group())


def match_zero_or_one_occurrence():
    """
    Match zero or one occurrence.
    """
    pattern = re.compile(r'a?b')
    result = pattern.search('b')
    if result:
        print("Pattern found:", result.group())


def use_character_classes():
    """
    Use character classes.
    """
    pattern = re.compile(r'[abc]')
    result = pattern.search('def')
    if result:
        print("Pattern found:", result.group())


def use_quantifiers():
    """
    Use quantifiers.
    """
    pattern = re.compile(r'a{3}')
    result = pattern.search('aaab')
    if result:
        print("Pattern found:", result.group())


def use_groups():
    """
    Use groups.
    """
    pattern = re.compile(r'(ab)+')
    result = pattern.search('ababab')
    if result:
        print("Pattern found:", result.group())


def use_alternation():
    """
    Use alternation.
    """
    pattern = re.compile(r'cat|dog')
    result = pattern.search('dog')
    if result:
        print("Pattern found:", result.group())


if __name__ == "__main__":
    match_literal_characters()
    match_any_single_character()
    match_beginning_of_string()
    match_end_of_string()
    match_zero_or_more_occurrences()
    match_one_or_more_occurrences()
    match_zero_or_one_occurrence()
    use_character_classes()
    use_quantifiers()
    use_groups()
    use_alternation()
