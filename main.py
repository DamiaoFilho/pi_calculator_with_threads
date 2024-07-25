import random
import time
import threading

def calculate_pi(point_quantity):
    points_inside = 0

    for i in range(point_quantity):
        x, y = random.random(), random.random()

        center_distance = x**2 + y**2
        if center_distance <= 1:
            points_inside += 1
        
    estimated_pi = 4 * points_inside / point_quantity
    return estimated_pi


threads_sum = []

def calculate_points_inside(point_quantity):
    points_inside = 0
    for i in range(point_quantity):
        x, y = random.random(), random.random()

        center_distance = x**2 + y**2
        if center_distance <= 1:
            points_inside += 1
        
    threads_sum.append(points_inside)



if __name__ == '__main__':
    print("Points quantity")
    point_quantity = int(input())

    print("Threads quantity")
    threads_quantity = int(input())
    
    print("Starting...")
    start_time = time.time()

    threads_list = []
    for i in range(threads_quantity):
        points_inside  = 0
        start = i * (point_quantity/threads_quantity)
        end = (i + 1) * (point_quantity/threads_quantity)
        thread_range = int(end)-int(start)
        t = threading.Thread(target=calculate_points_inside, args=[thread_range])
        threads_list.append(t)
        
    for t in threads_list:
        t.start()

    for t in threads_list:
        t.join()
        
    pi = 4 * sum(threads_sum)/point_quantity
    end_time = time.time()
    print("End.")




    print(f"Aproximação de π com {point_quantity} pontos e {threads_quantity} threads é: {pi}")
    print(f"Tempo de execução: {end_time - start_time} segundos")