# Задане речення
line = input("Введіть речення: ")

# Розділяємо речення на слова
words = line.split()

# Ініціалізуємо змінну для збереження довжини найкоротшого слова
shortest_word_lenght = len(words[0])

# Проходимося по кожному слову у реченні
for word in words:

    # Оновлюємо значення, якщо знайдено слово з коротшою довжиною
    if len(word) < shortest_word_lenght:
        shortest_word_lenght = len(word)

# Виводимо результат
print("Довжина найкоротшого слова у реченні:", shortest_word_lenght)
