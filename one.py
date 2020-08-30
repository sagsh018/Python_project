def func():
    print("FUNC() at top level in ONE.PY")


print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    print("ONE.PY is run directly")
else:
    print("ONE.PY is imported")
