from nornir import InitNornir
import random
import time

def my_task(task):
    time.sleep(random.random())
    print("-" * 20)
    print("hello from", task.host.hostname)
    print(" dns1:", task.host['dns1'])
    print(" dns2:", task.host['dns2'])

def main():
    nr = InitNornir()
    nr.run(task=my_task)

if __name__ == "__main__":
    main()
