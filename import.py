from os import name, system, startfile
from sys import argv
from glob import glob
from time import time

global _nt
_nt = name == "nt"

if _nt: from msvcrt import getch
else: from getch import getch

def import_replays(folder):
    idx = 0
    if not _nt: osu_path = input("[Linux detected] What is the path to your osu.exe? (e.g. /home/gamer123/osu.exe)")

    replays = glob(f"{argv[1]}/*.osr")
    l_replays = len(replays)

    print(f"Found {l_replays} replays. Beginning parse.\n")

    for idx, replay in enumerate(replays):
        _i = 1 + idx
        if _nt: startfile(replay, "open") # startfile is windows exclusive
        else: system("%s '%s'" % (osu_path, replay))

        # Print for every 25 replays.
        if not _i % 25: print(f"Progress {'%.2f' % (_i / l_replays * 100)}% ({_i} replays).")

    if not idx: raise Exception("Could not find any replays to import.")

if __name__ == "__main__":
    if len(argv) <= 1: raise Exception("Please provide a folder with replays to parse.")

    print("Feeding osu! replays.. Your osu! window will likely turn into a black screen due to the stress, don't worry.\nIf you wish to close the program at any time, you can use Ctrl + C (KeyboardInterrupt).\n")

    start_time = time()

    for folder in argv[1:]:
        print(f"Parsing folder {folder}.")
        import_replays(folder)

    execution_time = time() - start_time
    
    print("\nPress any key to exit - ", end='')
    if execution_time < 1: print("%.3fms." % (execution_time * 1000))
    else: print("%.3fs." % (time() - start_time))
    getch()