import sys
def safe_float(value):
    try:
        f = float(value)
        if f != f:
            return None
        return f
    except ValueError:
        return None

def read_numbers_from_csv(path):
    """Read numeric values from a CSV file (one value per line).

    BUGS: this function does not correctly handle invalid values or empty lines.
    """
    numbers = []
    with open(path, "r") as f:
        for line in f:
            value = line.strip()
            if not value:
                continue
            num = safe_float(value)
            if num is not None:
            # TODO: convert value to float and add to numbers
            # HINT: you should skip values that cannot be converted
                numbers.append(num)
    return numbers

def compute_mean(values):
    """Return the mean of a list of numbers.

    BUGS: implementation is incomplete / incorrect.
    """
    if not values:
        return None
    total = 0
    for v in values:
        total += v  # BUG: this is wrong
    return total / len(values)

def compute_median(values):
    """Return the median of a list of numbers.

    BUGS: does not handle even-length lists or empty lists correctly.
    """
    # TODO: implement proper median
    if not values:
        return None
    values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter.py <data.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    nums = read_numbers_from_csv(csv_path)
    
    if not nums:
        print("No valid numeric values found in file.")
        sys.exit(0)
    print("Read values:", nums)

    mean_val = compute_mean(nums)
    median_val = compute_median(nums)

    print("Mean:", mean_val)
    print("Median:", median_val)

if __name__ == "__main__":
    main()
