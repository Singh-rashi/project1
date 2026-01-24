def estimate_complexity(code):
    if "for" in code and "for" in code:
        return "O(n²)"
    elif "for" in code or "while" in code:
        return "O(n)"
    else:
        return "O(1)"
