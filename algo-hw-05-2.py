# Шляхи до текстових файлів
import os
import timeit
path1 = r"C:\Users\Ігор\Downloads\стаття 1.txt"
path2 = r"C:\Users\Ігор\Downloads\стаття 2 (1).txt"

# Завантаження текстів з правильним кодуванням
with open(path1, encoding="cp1251") as f1, open(path2, encoding="cp1251") as f2:
    text1 = f1.read()
    text2 = f2.read()

# Реалізація алгоритму Боєра-Мура


def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    # Таблиця зсувів
    bad_char_shift = {char: m - idx - 1 for idx, char in enumerate(pattern)}
    bad_char_shift.setdefault(None, m)

    idx = 0
    while idx <= n - m:
        for j in range(m - 1, -1, -1):
            if text[idx + j] != pattern[j]:
                idx += bad_char_shift.get(text[idx + j], bad_char_shift[None])
                break
        else:
            return idx  # Знайдено
    return -1  # Не знайдено

# Реалізація алгоритму Кнута-Морріса-Пратта (KMP)


def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    # Побудова таблиці префіксів
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    i, j = 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  # Знайдено
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # Не знайдено

# Реалізація алгоритму Рабіна-Карпа


def rabin_karp_search(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    # Хешування
    base = 256
    pattern_hash = 0
    text_hash = 0
    h = 1
    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i  # Знайдено
        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return -1  # Не знайдено


# Шляхи до текстових файлів
path1 = r"C:\Users\Ігор\Downloads\стаття 1.txt"
path2 = r"C:\Users\Ігор\Downloads\стаття 2 (1).txt"

# Перевірка існування файлів
if not os.path.exists(path1) or not os.path.exists(path2):
    print("Один або обидва файли не знайдені. Перевірте шляхи до файлів.")
else:
    # Завантаження текстів
    with open(path1, encoding="utf-8") as f1, open(path2, encoding="utf-8") as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Підрядки
    existing_substring = "структури даних"  # Існує в обох текстах
    nonexistent_substring = "вигаданий підрядок"  # Не існує

    # Вимірювання часу для кожного алгоритму
    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search,
    }

    results = {}

    for text, name in [(text1, "Text 1"), (text2, "Text 2")]:
        results[name] = {}
        for pattern, pattern_name in [(existing_substring, "Existing"), (nonexistent_substring, "Nonexistent")]:
            for algo_name, algo in algorithms.items():
                time_taken = timeit.timeit(
                    lambda: algo(text, pattern), number=100)
                results[name][f"{algo_name} ({pattern_name})"] = time_taken

    # Виведення результатів
    for text_name, timings in results.items():
        print(f"\nРезультати для {text_name}:")
        for algo, time_taken in timings.items():
            print(f"{algo}: {time_taken:.6f} секунд")
