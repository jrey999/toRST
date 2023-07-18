from toRST.toRST import Table
from funcs.command import parser, get_file_name


args = parser.parse_args()
def torst():
  
  for file in args.files:

    with open(f"{args.output_dir}/{get_file_name(file)}.rst", "w") as f:
        
        for line in Table(file).build_table():
            f.writelines(line + "\n")

if __name__ == "__main__":
    torst()