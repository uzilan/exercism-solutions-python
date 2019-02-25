def hey(phrase):
    stripped = phrase.strip()
    if not stripped:
        return "Fine. Be that way!"
    elif phrase.isupper():
        if stripped.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif stripped.endswith('?'):
        return "Sure."
    else:
        return "Whatever."
