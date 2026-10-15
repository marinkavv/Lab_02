import threading  # робота з потоками
import fixed  # імпортуємо виправлену програму

# тест на перевірку стану гонки
def test_balance_not_negative():

    fixed.balance = 1000  # встановлюю початковий баланс

    # створюю потоки
    t1 = threading.Thread(target=fixed.transfer, args=(600, None))

    t2 = threading.Thread(target=fixed.transfer, args=(600, None))

    # запускаю потоки
    t1.start()
    t2.start()

    # очікую завершення
    t1.join()
    t2.join()

    # перевіряю правильність результату
    assert fixed.balance == 400, (
        f"Помилка! Очікуваний баланс: 400, " f"отриманий: {fixed.balance}"
    )
