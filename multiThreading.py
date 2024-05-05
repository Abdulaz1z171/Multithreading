# 2 ta database dan ma'lumotlarni bir sil vaqtda parallel ravishda ishlatish

import psycopg2
import threading
import time
from colorama import Fore


def print_for_n42(message):
    
    print(Fore.GREEN + message + Fore.RESET)

def print_for_my_project(message):
    print(Fore.BLUE + message + Fore.RESET)




def get_information_from_n42_db():
    conn_n42_db = psycopg2.connect(
    database = 'n42',
    host = 'localhost',
    password = 'temur_1336',
    user = 'postgres',
    port = 5432)
    cur_n42 = conn_n42_db.cursor()
    select_query = 'SELECT * FROM books;'
    cur_n42.execute(select_query)
    conn_n42_db.commit()
    for book in cur_n42.fetchall():
        print_for_n42(str(book))
        time.sleep(1)

def get_information_from_my_project_db():
    conn_my_project_db = psycopg2.connect(
    database = 'my_project',
    host = 'localhost',
    password = 'temur_1336',
    user = 'postgres',
    port = 5432)
    cur_my_project = conn_my_project_db.cursor()
    select_query = 'SELECT * FROM person;'
    cur_my_project.execute(select_query)
    conn_my_project_db.commit()
    for human in cur_my_project.fetchall():
        print_for_my_project(str(human))
        time.sleep(1)





if __name__ == '__main__':
    thread1 = threading.Thread(target = get_information_from_n42_db)
    thread2 = threading.Thread(target = get_information_from_my_project_db)


    start_time = time.time()

    thread1.start()
    thread2.start()



    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'This operation take in {end_time - start_time}')