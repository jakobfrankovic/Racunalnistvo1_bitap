def bitap_fuzzy_bitwise_search(text, pattern, k):
    m = len(pattern)
    R = [~1] * (k+1)
    pattern_mask = [~0] * (2**8)  # 2**8 is the number of ASCII characters
    for i in range(m):
        pattern_mask[ord(pattern[i])] &= ~(1 << i)
    for i in range(len(text)):
        old_Rd1 = R[0]
        R[0] |= pattern_mask[ord(text[i])]
        R[0] <<= 1
        for d in range(1, k+1):
            tmp = R[d]
            R[d] = (old_Rd1 & (R[d] | pattern_mask[ord(text[i])])) << 1
            old_Rd1 = tmp
        if R[k] & (1 << m) == 0:
            return text[i-m+1:]
    return None
print(bitap_fuzzy_bitwise_search("JanezSe UciZaIzpit", "e zmlt", 4))