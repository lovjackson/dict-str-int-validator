from validator import ensure_dict_str_int

@ensure_dict_str_int
def process_data(data: dict[str, int]) -> int:
    return sum(data.values())

if __name__ == "__main__":
    print(process_data({"a": 1, "b": 2}))  # Works: 3
