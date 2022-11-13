def multiple_letter_count(phrase):
    dict={}

    for ltr in phrase:
        dict[ltr]=dict.get(ltr, 0)+1
    return dict

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """