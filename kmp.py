# python3
import sys


def compute_prefix_function(text):
    t_len = len(text)
    s = [0] * t_len
    border = 0

    for i in range(1, t_len):
        while (border > 0) and (text[i] != text[border]):
            border = s[border - 1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    p_len = len(pattern)
    t_len = len(text)
    result = []
    ref_str = "".join([pattern, "$", text])
    rs_len = len(ref_str)

    prefix_arr = compute_prefix_function(ref_str)
    for i in range(p_len+1, rs_len):
        if prefix_arr[i] == p_len:
            result.append(i - 2*p_len)
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

