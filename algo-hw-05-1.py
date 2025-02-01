class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if not self.table[key_hash]:  # Перевірка на порожній список
            self.table[key_hash] = [key_value] # Створення списку з елементом
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]: # Перевірка на порожній список
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:  # Перевірка, чи є що видаляти
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True  # Повертаємо True, якщо успішно видалено
            return False #Повертаємо False, якщо ключ не знайдено
        return False #Повертаємо False, якщо за даним індексом нічого немає


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))    # Виведе: 10
print(H.get("orange"))   # Виведе: 20
print(H.get("banana"))   # Виведе: 30

H.delete("orange")
print(H.get("orange"))   # Виведе: None

print(H.delete("grape")) #Виведе False

H.insert("grape", 40)
print(H.get("grape")) #Виведе 40

H.delete("grape")
print(H.get("grape")) #Виведе None

H.delete("apple")
print(H.get("apple")) #Виведе None

H.delete("banana")
print(H.get("banana")) #Виведе None
