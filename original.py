
import threading  # бібліотека для роботи з потоками
import time  # бібліотека для затримок

balance = 1000  # початковий баланс рахунку

lock = threading.Lock()  # створюємо блокування, але не використовуємо його


# функція для переказу коштів
def transfer(amount, recipient_func):
    global balance  # використовуємо спільну змінну

    local_balance = balance  # зчитуємо поточний баланс

    time.sleep(0.01)  # імітуємо затримку

    # Перевіряємо, чи вистачає грошей
    if local_balance >= amount:

        print(
            f"Потік {threading.current_thread().name} "
            f"перевіряє баланс: {local_balance}"
        )

        time.sleep(0.01)  # додаткова затримка

        balance -= amount  # зменшуємо баланс

        print(
            f"Потік {threading.current_thread().name} "
            f"переказав {amount}. Новий баланс: {balance}"
        )

    else:
        print(
            f"Потік {threading.current_thread().name} "
            f"не зміг переказати {amount}. "
            f"Недостатньо коштів."
        )


if __name__ == "__main__":

    # створюємо два потоки
    t1 = threading.Thread(
        target=transfer,
        args=(600, None),
        name="Потік-1"
    )

    t2 = threading.Thread(
        target=transfer,
        args=(600, None),
        name="Потік-2"
    )

    # запускаємо обидва потоки
    t1.start()
    t2.start()

    # Очікуємо завершення потоків
    t1.join()
    t2.join()

    # виводимо кінцевий баланс
    print(f"\nКінцевий баланс: {balance}")
