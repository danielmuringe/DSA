from json import load
from pathlib import Path
from sys import path as sys_path

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# Import dynamic solution module
sys_path.append(str(BASE_DIR / "src"))
dynamic_solution = __import__("dynamic_solution")

# Get test cases
TESTS_PATH = BASE_DIR / "tests.json"
with open(TESTS_PATH) as TESTS_FILE:
    TEST_CASES = load(TESTS_FILE)


for test_case in TEST_CASES:
    expected_lccs_vals = set([tuple(x) for x in test_case["expected_lccs_vals"]])
    pair = [tuple(x) for x in test_case["pair"]]

    min_i, lccs_size, lccs_starts = dynamic_solution.lccs(*pair)

    actual_lccs_vals = set(
        [pair[min_i][lccs_start : lccs_start + lccs_size] for lccs_start in lccs_starts]
    )

    _match = "" if (expected_lccs_vals == actual_lccs_vals) else "\t\t\tDO NOT MATCH"

    print("PAIR: ", pair, _match)
    print("EXPECTED: ", expected_lccs_vals)
    print("ACTUAL: ", actual_lccs_vals)
    print()
