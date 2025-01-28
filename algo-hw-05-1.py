def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]  # Якщо знайдено точний збіг

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]  # Оновлюємо верхню межу
            right = mid - 1

    # Якщо target не знайдено, повертаємо найменший елемент, який є більшим або рівним
    return iterations, upper_bound


# Приклад використання
sorted_array = [0.5, 1.2, 2.4, 3.7, 4.1, 5.6, 7.3]
target_value = 3.0

result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (кількість ітерацій, верхня межа)
