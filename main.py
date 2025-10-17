import sys

try:
    import pyperclip
except ImportError:
    print("Error: Missing Python module. Please install 'pyperclip' before running this script.")
    sys.exit(1)


if __name__ == "__main__":
    includes: str = pyperclip.paste()
    includes_lines: list[str] = [
        line.split("//")[0].strip()
        for line in includes.splitlines()
    ]

    pos: int = -1
    for idx, line in enumerate(includes_lines):
        if line.startswith("namespace"):
            pos: int = idx
            break

    if pos > 0:
        includes_lines.insert(pos, "")

    pyperclip.copy("\n".join(includes_lines))
