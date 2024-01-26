#Jason Martin
#90501948

#program that streams about 1kb of text at a time from an input file, reverses it, and writes it to an output file.

import argparse
CHUNK_SIZE = 1024 #about 1 kilobyte worth of characters


def write(reverse_text, output_file):
    current_chunk = reverse_text[:CHUNK_SIZE] #grabs one kb worth of characters from the reversed input file
    counter = 1 #counter to increment through the reversed input file by kbs
    try:
        with open(output_file, "w") as f_out:
            while True:
                f_out.write(current_chunk)
                current_chunk = reverse_text[CHUNK_SIZE * counter: CHUNK_SIZE * (counter + 1)] #increments through the reversed input file kb by kb
                counter += 1
                if not current_chunk: #exits the loop when the end of the reversed input file has been reached
                    break
    except IOError as e:
        print(f"IO Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def reverse_text(input_file): #streams from the input file and reverses each chunk as it is read
    reverse_chunk = ""
    reverse_text = ""
    try:
        with open(input_file, "r") as f_in:
            while True:
                chunk = f_in.read(CHUNK_SIZE)
                #exit the loop when the end of the file is reached
                if not len(chunk) > 0:
                    break

                reverse_chunk = chunk[::-1]
                reverse_text = reverse_chunk + reverse_text #appends the total reversed text to the end of the newly reversed chunk to mimic an actually reversed string
        return reverse_text
    except FileNotFoundError as e:
        print(f"Error: {input_file} not found")
    except Exception as e:
        print(f"Error: {e}")




def take_input(): #receives the input file and output file names as input from the command line
    parser = argparse.ArgumentParser() #creates parser

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