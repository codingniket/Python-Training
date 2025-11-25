
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted

# Example usage:
input_dict = {"a": 1, "b": 2, "c": 1}
output_dict = invert_dict(input_dict)
