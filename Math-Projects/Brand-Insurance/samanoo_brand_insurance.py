input_string = input()

if "m" in input_string:
    print('No')
else:
    print('Yes')

if __name__ == "__main__":
    # ---- Test Cases ----
    test_inputs = [
        ("bitpin", "Yes"),
        ("samanoo", "No"),
        ("hello", "Yes"),
        ("mango", "No"),
        ("m", "No"),
        ("abc", "Yes"),
        ("mmmmmmm", "No"),
        ("abcdefghijklmnopqrst", "No"),
        ("mmmmmmmmmmmmmmmmmmmm", "No"),  # length 20 with 'm'
        ("moment", "No"),
        ("Memory", "No"),
    ]

    print("\nRunning Tests...")
    for text, expected in test_inputs:
        result = "No" if "m" in text else "Yes"
        status = "✔ PASSED" if result == expected else "❌ FAILED"
        print(f"Input: {text:<22} Expected: {expected:<3}  Got: {result:<3} --> {status}")
