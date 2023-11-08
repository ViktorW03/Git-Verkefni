
import sys
def state_music_opinion(genre = "Classic rock", music_group = "The Beatles", vocalist = "Freddie Mercury"):
    print(f"The best type of music is {genre}.")
    print(f"The best music group is {music_group}.")
    print(f"The best lead vocalist is {vocalist}.")
    

def main():
    # Simple test script.
    sys.stderr.write("Input music, group, singer: ")
    music, group, singer = input().split(",")
    print(state_music_opinion())


# Definition for state_music_opinion goes here.


if __name__ == "__main__":
    main()
