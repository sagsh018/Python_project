import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print("TWO.PY has been called directly")
else:
    print("TWO.PY has been imported")
