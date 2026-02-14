import random
import os

def clear_console():
    """Очищает консоль для лучшей читаемости (работает на Windows и Unix)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_console()
    
    print("=" * 50)
    print("ИГРА 'РОМАШКА'")
    print("=" * 50)
    print("\nЗагадай желание!")
    print("Сейчас мы будем гадать на ромашке: 'Любит - не любит'")
    
    # Проверка ввода начального значения
    while True:
        print("\nС чего начнем?")
        print("1 - Любит")
        print("2 - Не любит")
        
        try:
            start_choice = input("Введите 1 или 2: ").strip()
            
            if start_choice in ['1', '2']:
                break
            else:
                print("Ошибка! Пожалуйста, введите 1 или 2.")
        except KeyboardInterrupt:
            print("\n\nИгра прервана. До свидания!")
            return
    
    # Генерируем случайное количество лепестков (от 6 до 10)
    petals = random.randint(6, 10)
    
    # Определяем начальное слово
    current_word = "Любит" if start_choice == '1' else "Не любит"
    
    print(f"\nНачинаем гадание! Количество лепестков неизвестно...")
    print(f"Первое слово: {current_word}")
    print("\nНажимай Enter, чтобы отрывать лепестки...")
    
    # Основной игровой цикл
    for i in range(petals - 1):  # -1 потому что первый лепесток мы уже показали
        input()
        
        # Меняем слово на противоположное
        if current_word == "Любит":
            current_word = "Не любит"
        else:
            current_word = "Любит"
        
        print(current_word)
    
    # Последний Enter для завершения
    input()
    
    # Финальный результат
    clear_console()
    print("=" * 50)
    print("РЕЗУЛЬТАТ ГАДАНИЯ")
    print("=" * 50)
    print(f"\nНа ромашке было {petals} лепестков.")
    print(f"И последнее слово: {current_word}!")
    
    if current_word == "Любит":
        print("\n✨ Поздравляю! Похоже, вас любят! ✨")
    else:
        print("\n💔 Не расстраивайтесь, это всего лишь игра! 💔")
    
    print("\n" + "=" * 50)

def main():
    while True:
        play_game()
        
        print("\nХотите сыграть еще раз?")
        again = input("Введите 'да' для новой игры, или что угодно для выхода: ").strip().lower()
        
        if again != 'да':
            print("\nСпасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nИгра прервана. До свидания!")