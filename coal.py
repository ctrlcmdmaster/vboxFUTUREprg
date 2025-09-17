import webbrowser

BANNER = """
===============================
   Vbox FUTURE - Coal Interface
===============================
Type 'run [program]' to launch.
Type 'exit' to quit.
"""

BASE_URL = "https://ctrlcmdmaster.github.io/vboxFUTUREprg/"

def main():
    print(BANNER)
    while True:
        cmd = input("coal> ").strip()
        
        if cmd.lower() == "exit":
            print("Exiting Coal Interface...")
            break
        
        elif cmd.lower().startswith("run "):
            program = cmd[4:].strip()
            if program:
                url = f"{BASE_URL}{program}.html"
                print(f"Launching {program} at {url}")
                webbrowser.open(url)
            else:
                print("Error: No program specified. Usage: run [program]")
        
        elif cmd == "":
            continue
        
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
