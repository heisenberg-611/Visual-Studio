if picked == 'S' and is_max:
    multiplier = (first_two_digits) / 100
    new_weights[i:] = [w * multiplier for w in weights[i:]]