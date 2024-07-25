import random
import time
import threading
from matplotlib import pyplot as plt

def calculate_pi(point_quantity):
    points_inside = 0

    for i in range(point_quantity):
        x, y = random.random(), random.random()

        center_distance = x**2 + y**2
        if center_distance <= 1:
            points_inside += 1
        
    estimated_pi = 4 * points_inside / point_quantity
    return estimated_pi



def calculate_points_inside(point_quantity):
    points_inside = 0
    for i in range(point_quantity):
        x, y = random.random(), random.random()

        center_distance = x**2 + y**2
        if center_distance <= 1:
            points_inside += 1
        
    threads_sum.append(points_inside)


if __name__ == '__main__':

    print("Threads quantity")
    threads_quantity = int(input())
    

    points_vector = [100000, 250000, 1000000]
    times = []
    normal_times = []

    for pv in points_vector:
        print("Starting...", pv)

        start_time = time.time()

        threads_sum = []
        threads_list = []

        for i in range(threads_quantity):
            points_inside  = 0
            start = i * (pv/threads_quantity)
            end = (i + 1) * (pv/threads_quantity)
            thread_range = int(end)-int(start)
            t = threading.Thread(target=calculate_points_inside, args=[thread_range])
            threads_list.append(t)
            
        for t in threads_list:
            t.start()

        for t in threads_list:
            t.join()
        
        pi = 4 * sum(threads_sum)/pv

        end_time = time.time()
        threads_time = end_time - start_time
        times.append(threads_time)

        print("End.")
        print(f"Time: {threads_time}\nResult: {pi}")

        print("Starting normal...", pv)
        start_time = time.time()  
        pi_estimado = calculate_pi(pv)
        end_time = time.time()  
        normal_time = end_time - start_time
        normal_times.append(normal_time)
        print("End.", pi_estimado)
        print(f"Time: {normal_time}\nResult: {pi_estimado}")



plt.title("Time by Vector Length")
plt.xlabel("Points")
plt.ylabel("Time")
plt.plot(points_vector, times, label="Threads", marker="o")
plt.plot(points_vector, normal_times, label="Normal", marker="o")
plt.yscale("symlog")
plt.xscale("symlog")
plt.legend(["Threads", "Normal"])
plt.grid(True)
plt.show()