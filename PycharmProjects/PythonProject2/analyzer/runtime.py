import time


def measure_runtime(code):
    results = []
    local_env = {}

    for n in [100, 500, 1000]:
        wrapped_code = f"""
def test(n):
{indent_code(code)}

test({n})
"""
        try:
            start = time.time()
            exec(wrapped_code, {}, local_env)
            end = time.time()
            results.append((n, round(end - start, 6)))
        except Exception:
            results.append((n, "Error"))

    return results


def indent_code(code):
    return "\n".join("    " + line for line in code.split("\n"))
