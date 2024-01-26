#Jason Martin
#90501948
import argparse
CHUNK_SIZE = 1024

def write(input_file, output_file):
    with open(output_file, "w") as f:
        while True:
            #exit the loop when the end of the file is reached
            if not len(chunk) > 0:
                break
            
            #reversed_text = reverse_chunk + reverse_text'''


def read(input_file):
    reversed_chunk = ""
    with open(input_file, "r") as f:
        chunk = f.read(CHUNK_SIZE)
        reversed_chunk = chunk[::-1]
    return reversed_chunk


def take_input():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    return (input_file, output_file)

def main():
    input_file, output_file = take_input()
    write(input_file, output_file)

if __name__ == "__main__":
    main()