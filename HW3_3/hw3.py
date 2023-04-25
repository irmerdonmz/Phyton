# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
def custom_range(sequence, stop, start=None, step=1):
    """
    Returns a list of values from the sequence starting from the start value (default is None)
    up to, but not including, the stop value, with an optional step value (default is 1).
    """
    if start is None:
        start = sequence[0]
    else:
        assert start in sequence, "Start value must be in the sequence."

    assert stop in sequence, "Stop value must be in the sequence."
    assert step != 0, "Step value cannot be zero."

    start_idx = sequence.index(start)
    stop_idx = sequence.index(stop)
    step = abs(step) if stop_idx > start_idx else -abs(step)

    return list(sequence[start_idx:stop_idx:step])

    import string

    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']