import argparse
import json
from gendiff import generate_diff


def read_json(file_path):
    """Lee un archivo JSON y devuelve su contenido como diccionario."""
    with open(file_path) as f:
        return json.load(f)



def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=["plain", "json"],
        default="plain"
    )

    args = parser.parse_args()

    # data1 = read_json(args.first_file)
    # data2 = read_json(args.second_file)

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
    # print("Contenido json del primer archivo:", data1)
    # print("Contenido json del segundo archivo:", data2)
    # print(f"Comparing '{args.first_file}' with '{args.second_file}' using format '{args.format}'")

if __name__ == "__main__":
    main()