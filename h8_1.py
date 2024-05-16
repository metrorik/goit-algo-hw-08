import heapq

def min_cost_to_connect_cables(cables):
    # min купа з початкового списку довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        combined_length = first + second
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, combined_length)
        
        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += combined_length
    
    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
print(f"Мінімальні загальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cable_lengths)}")

# Вибираючи завжди найменші елементи для об'єднання, проміжні суми завжди мінімальні. 
# Це запобігає накопиченню великих значень, які зазвичай призводять до більших загальних витрат.