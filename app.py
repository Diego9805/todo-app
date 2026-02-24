tasks = []

while True:
    task = input("Nueva tarea: ")
    tasks.append(task)

    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")

    print(tasks)