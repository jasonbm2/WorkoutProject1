#Jason Martin
#90501948

#simple program that streams about 1kb of text at a time from an input file, reverses it, and writes it to an output file.

import argparse
CHUNK_SIZE = 1024

def write(reverse_text, output_file):
    current_chunk = reverse_text[:CHUNK_SIZE]
    counter = 1
    with open(output_file, "w") as f_out:
        while True:
            f_out.write(current_chunk)
            current_chunk = reverse_text[CHUNK_SIZE * counter: CHUNK_SIZE * (counter + 1)]
            counter += 1
            if not current_chunk:
                break



def reverse_text(input_file):
    reverse_chunk = ""
    reverse_text = ""
    with open(input_file, "r") as f_in:
        while True:
            chunk = f_in.read(CHUNK_SIZE)
            #exit the loop when the end of the file is reached
            if not len(chunk) > 0:
                break

            reverse_chunk = chunk[::-1]
            reverse_text = reverse_chunk + reverse_text
    return reverse_text


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
    write(reverse_text(input_file), output_file)

if __name__ == "__main__":
    main()