def main():
    USI_Ponder = "USI_Ponder"
    USI_Hash = "USI_Hash"

    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            continue

        tokens = line.split()
        if not tokens:
            continue

        command = tokens[0]

        match command:
            case "usi":
                print("id name rei", flush=True)
                print("id author kazuro noguchi", flush=True)
                print(
                    f"option name {USI_Ponder} type check default true", flush=True)
                print(
                    f"option name {USI_Hash} type spin default 256", flush=True)
                print("usiok", flush=True)
            case "isready":
                print("readyok", flush=True)
            case "usinewgame" | "setoption" | "position" | "stop" | "ponderhit" | "gameover":
                pass
            case "go":
                print("bestmove resign", flush=True)
            case "quit":
                break
            case _:
                print(
                    f"info string Unsupported command: {command}", flush=True)


if __name__ == '__main__':
    main()
