def alternating_case(s):
    result = []
    toggle = True
    for char in s:
        if char.isalpha():
            result.append(char.upper() if toggle else char.lower())
            toggle = not toggle
        else:
            result.append(char)
    return "".join(result)

# Test Cases
print(alternating_case("hello world!"))  # "HeLlO wOrLd!"
print(alternating_case("abc123! xyz"))  # "AbC123! xYz"

# Test for:
print(alternating_case("Za^B8g@E2jH*kWl!MoPqXr7YvT1c$Fs3Ud9IwZ&yX0pLkV6sHqN^tB4rA+oZ%gFj"))  # Output?
