from csv2rst.csv2rst import Table as CSVTable
from funcs.command import parser, get_file_name, get_extension


args = parser.parse_args()
for file in args.files:

    if get_extension(file) == "csv":


        with open("{}/{}.rst".format(args.output_dir, get_file_name(file)), "w") as f:
            for line in CSVTable(file).build_table():
                f.writelines(line + "\n")

    else:
        raise ValueError("{} files are not supported".format(get_extension(file).upper()))