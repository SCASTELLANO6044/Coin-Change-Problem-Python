import Memoization
import Tabulation

# Inicio del programa.

# tab = False
# mem = False
# both = False
# isDirectory = False
#
# valid_first = ["-d", "--directory", "-f", "--file", "-h", "--help"]
# valid_second = ["-sm", "--memoization", "-st", "--tabulation", "--check"]
#
# if sys.argv[1] == "-h" or sys.argv[1] == "--help":
#     print("Uso del programa: CoinChangeProblem.py [-d [DIRECTORY] | -f [FILE]] [-sm | -st | -check]\n\n" +
#           "optional arguments:\n" +
#           "    -d [DIRECTORY], --directory [DIRECTORY]     process many files in a directory\n" +
#           "    -f [FILE], --file [FILE]                    process a single file\n" +
#           "    -sm, --memoization                          count number of combinations to reach the change with the available coins through Memoization\n" +
#           "    -st, --tabulation                           count number of combinations to reach the change with the available coins through Tabulation\n" +
#           "    --check                                     check that the count number of combinations to reach the change with the available coins\n" +
#           "                                                    is the same through Tabulation and Memoization\n")
# elif sys.argv[1] not in valid_first or sys.argv[3] not in valid_second:
#     print("No ha escrito los parámetros de entrada del programa correctamente:\n"
#           "Uso del programa: CoinChangeProblem.py [-d [DIRECTORY] | -f [FILE]] [-sm | -st | -check]\n\n" +
#           "optional arguments:\n" +
#           "    -d [DIRECTORY], --directory [DIRECTORY]     process many files in a directory\n" +
#           "    -f [FILE], --file [FILE]                    process a single file\n" +
#           "    -sm, --memoization                          count number of combinations to reach the change with the available coins through Memoization\n" +
#           "    -st, --tabulation                           count number of combinations to reach the change with the available coins through Tabulation\n" +
#           "    --check                                     check that the count number of combinations to reach the change with the available coins\n" +
#           "                                                    is the same through Tabulation and Memoization\n")
# else:
#     second_param = ""
#
#     if sys.argv[1] == valid_first[0] or sys.argv[1] == valid_first[1]:
#         isDirectory = True
#         second_param = sys.argv[2]
#         print(second_param)
#     elif sys.argv[1] == valid_first[2] or sys.argv[1] == valid_first[3]:
#         second_param = sys.argv[2]
#
#     if sys.argv[3] == valid_second[4]:
#         tab = False
#         mem = False
#         both = True
#     elif sys.argv[3] == valid_second[0] or sys.argv[3] == valid_second[1]:
#         tab = False
#         mem = True
#         both = False
#     elif sys.argv[3] == valid_second[2] or sys.argv[3] == valid_second[3]:
#         tab = True
#         mem = False
#         both = False


coins = [1, 2, 3]
memory = {}
combinations = Memoization.execute(coins, len(coins)-1, 4, memory)
numOfCombinations = len(combinations)
print(numOfCombinations)
for combination in combinations:
    print(combination)

tabulation = Tabulation.execute(coins, 4)
print(tabulation)

