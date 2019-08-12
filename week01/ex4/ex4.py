from nornir import InitNornir

def my_task(task):
    print("hello from", task.host.hostname)
    print("my group is", task.host.groups)

def main():
    nr = InitNornir()
    nr.run(task=my_task)

if __name__ == "__main__":
    main()
