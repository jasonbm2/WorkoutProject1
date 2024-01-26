#Jason Martin
#90501948
import argparse
CHUNK_SIZE = 1024

def write(input_file, output_file):
    with open(output_file, "w") as f_out:
        while True:
            chunk = read(input_file)
            #exit the loop when input_file is completely read
            if chunk == None:
                break
            f_out.seek(0,0) #moves cursor to beginning of write file
            f_out.write(chunk)


def read(input_file):
    reversed_chunk = ""
    with open(input_file, "r") as f_in:
        chunk = f_in.read(CHUNK_SIZE)
        if not chunk:
            return None #end of file reached
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