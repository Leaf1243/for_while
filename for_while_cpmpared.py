import csv
import random
import time

timer_func = time.perf_counter
dice_list = [1, 2, 3, 4, 5, 6]
fixed_choices = [random.choice(dice_list) for _ in range(100000)]
indices = list(range(100000))

# 1. forループの実験（先に実行）
print("forループの実験を開始中...")
execution_times_for = []

for loop_count in range(1000):
    start_time = timer_func()
    for i in indices:
        _ = fixed_choices[i]
    end_time = timer_func()
    execution_times_for.append(end_time - start_time)

# forの結果を保存
csv_file_name_for = "clean_simulation_times(for).csv"
with open(csv_file_name_for, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["試行回数", "処理時間(秒)"])
    for index, elapsed_time in enumerate(execution_times_for):
        writer.writerow([index + 1, f"{elapsed_time:.9f}"])

print(f"-> '{csv_file_name_for}' に保存しました。")


# 2. whileループの実験（続けて自動で実行）
print("whileループの実験を開始中...")
execution_times_while = []

for loop_count in range(1000):
    start_time = timer_func()
    i = 0
    while i < 100000:
        _ = fixed_choices[i]
        i = i + 1
    end_time = timer_func()
    execution_times_while.append(end_time - start_time)

# whileの結果を保存
csv_file_name_while = "clean_simulation_times(while).csv"
with open(csv_file_name_while, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["試行回数", "処理時間(秒)"])
    for index, elapsed_time in enumerate(execution_times_while):
        writer.writerow([index + 1, f"{elapsed_time:.9f}"])

print(f"-> '{csv_file_name_while}' に保存しました。")