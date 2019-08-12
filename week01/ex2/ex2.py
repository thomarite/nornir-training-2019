from nornir import InitNornir

def main():
    nr = InitNornir()
  
    for k,v in nr.inventory.hosts.items():
        print("-" * 20)
        print(f"Host: {k}")
        print(f"  hostname: {v.hostname}")
        print(f"  groups: {v.groups}")
        print(f"  platform: {v.platform}")
        print(f"  user: {v.username}")
        print(f"  pass: {v.password}")
        print(f"  port: {v.port}")

if __name__ == "__main__":
    main()
