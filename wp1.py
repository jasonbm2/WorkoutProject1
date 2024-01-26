#Jason Martin
#90501948
import argparse

def reverse_text(input_file, output_file):
    with open(input_file, "r") as f:
        current_line = f.readline()

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
    reverse_text(input_file, output_file)

if __name__ == "__main__":
    main()