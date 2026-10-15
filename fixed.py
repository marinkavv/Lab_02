import threading  # бібліотека для роботи з потоками
import time  # бібліотека для затримок

balance = 1000  # початковий баланс

lock = threading.Lock()  # створюю блокування

# функція для переказу коштів
def transfer(amount, recipient_func):
    global balance  # використовую спільну змінну

    # захищаю перевірку та зміну балансу
    with lock:

        local_balance = balance  # зчитую баланс

        time.sleep(0.01)  # імітую затримку

        # перевіряю наявність коштів
        if local_balance >= amount:

            print(
                f"Потік {threading.current_thread().name} "
                f"перевіряє баланс: {local_balance}"
            )

            time.sleep(0.01)

            balance -= amount  # зменшую баланс

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

    # створюю потоки
    t1 = threading.Thread(target=transfer, args=(600, None), name="Потік-1")

    t2 = threading.Thread(target=transfer, args=(600, None), name="Потік-2")

    # запускаю потоки
    t1.start()
    t2.start()

    # очікую завершення
    t1.join()
    t2.join()

    print(f"\nКінцевий баланс: {balance}")  # виводжу кінцевий баланс
