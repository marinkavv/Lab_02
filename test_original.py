import threading  # робота з потоками
import original  # початкова програма з помилкою


# тест на перевірку стану гонки
def test_balance_not_negative():

    
    original.balance = 1000 # встановлюю початковий баланс

    # створюю два потоки
    t1 = threading.Thread(target=original.transfer, args=(600, None))

    t2 = threading.Thread(target=original.transfer, args=(600, None))

    # Запускаю їх
    t1.start()
    t2.start()

    # І очікую завершнення
    t1.join()
    t2.join()

    # перевіряю правильність результату
    assert original.balance == 400, (
        f"Помилка! Очікуваний баланс: 400, " f"отриманий: {original.balance}"
    )
