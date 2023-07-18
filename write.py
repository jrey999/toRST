from toRST.toRST import Table
from funcs.command import parser, get_file_name


args = parser.parse_args()
for file in args.files:

    with open("{}/{}.rst".format(args.output_dir, get_file_name(file)), "w") as f:
        for line in Table(file).build_table():
            f.writelines(line + "\n")