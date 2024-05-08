import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0

    # Preprocess the pattern
    bad_char = {pattern[i]: i for i in range(m)}

    # Search for pattern in the text
    i = m - 1
    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # pattern found
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + bad_char.get(text[i], -1))
            j = m - 1
    return -1  # pattern not found


def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0

    # Preprocess the pattern
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    # Search for pattern in the text
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1  # pattern found
    return -1  # pattern not found


def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0

    # Calculate hash value for the pattern and the first window of text
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Search for pattern in the text
    for i in range(n - m + 1):
        if p == t:
            if pattern == text[i:i + m]:
                return i  # pattern found
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1  # pattern not found


with open("article_1.txt", "r", encoding="utf-8") as file:
    article_1 = file.read()

with open("article_2.txt", "r", encoding="utf-8") as file:
    article_2 = file.read()

existing_substring_1 = "Метою роботи є виявлення найбільш популярних алгоритмів у бібліотеках мов програмування."
existing_substring_2 = "Ключові слова: рекомендаційні системи, бази даних, структури даних, програмна імітаційна модель."
fake_substring = "fake_fake"

# Боєра-Мура
# existing_substring
time_bm_existing_article_1 = timeit.timeit(lambda: boyer_moore(article_1, existing_substring_1), number=1000)
time_bm_existing_article_2 = timeit.timeit(lambda: boyer_moore(article_2, existing_substring_2), number=1000)

# fake_substring
time_bm_fake_article_1 = timeit.timeit(lambda: boyer_moore(article_1, fake_substring), number=1000)
time_bm_fake_article_2 = timeit.timeit(lambda: boyer_moore(article_2, fake_substring), number=1000)

# КМП
# existing_substring
time_kmp_existing_article_1 = timeit.timeit(lambda: kmp_search(article_1, existing_substring_1), number=1000)
time_kmp_existing_article_2 = timeit.timeit(lambda: kmp_search(article_2, existing_substring_2), number=1000)

# fake_substring
time_kmp_fake_article_1 = timeit.timeit(lambda: kmp_search(article_1, fake_substring), number=1000)
time_kmp_fake_article_2 = timeit.timeit(lambda: kmp_search(article_2, fake_substring), number=1000)

# Рабіна-Карпа
# existing_substring
time_rk_existing_article_1 = timeit.timeit(lambda: rabin_karp(article_1, existing_substring_1), number=1000)
time_rk_existing_article_2 = timeit.timeit(lambda: rabin_karp(article_2, existing_substring_2), number=1000)

# fake_substring
time_rk_fake_article_1 = timeit.timeit(lambda: rabin_karp(article_1, fake_substring), number=1000)
time_rk_fake_article_2 = timeit.timeit(lambda: rabin_karp(article_2, fake_substring), number=1000)


print("Час виконання алгоритму Боєра-Мура для існуючого підрядка в тексті статті 1:", time_bm_existing_article_1)
print("Час виконання алгоритму Боєра-Мура для вигаданого підрядка в тексті статті 1:", time_bm_fake_article_1)
print("Час виконання алгоритму Боєра-Мура для існуючого підрядка в тексті статті 2:", time_bm_existing_article_2)
print("Час виконання алгоритму Боєра-Мура для вигаданого підрядка в тексті статті 2:", time_bm_fake_article_2)

print("Час виконання алгоритму КМП для існуючого підрядка в тексті статті 1:", time_kmp_existing_article_1)
print("Час виконання алгоритму КМП для вигаданого підрядка в тексті статті 1:", time_kmp_fake_article_1)
print("Час виконання алгоритму КМП для існуючого підрядка в тексті статті 2:", time_kmp_existing_article_2)
print("Час виконання алгоритму КМП для вигаданого підрядка в тексті статті 2:", time_kmp_fake_article_2)

print("Час виконання алгоритму Рабіна-Карпа для існуючого підрядка в тексті статті 1:", time_rk_existing_article_1)
print("Час виконання алгоритму Рабіна-Карпа для вигаданого підрядка в тексті статті 1:", time_rk_fake_article_1)
print("Час виконання алгоритму Рабіна-Карпа для існуючого підрядка в тексті статті 2:", time_rk_existing_article_2)
print("Час виконання алгоритму Рабіна-Карпа для вигаданого підрядка в тексті статті 2:", time_rk_fake_article_2)