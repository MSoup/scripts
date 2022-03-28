import re

def incrementVersion(filename):
  with open(filename, "r") as f:
    pattern = r"(version: \d.\d.\d\+)(\d+)"
    contents = f.read()

    x = re.search(pattern, contents)
    replacement = int(x[2]) + 1
    root = x[1]
    data = re.sub(pattern, root + str(replacement), contents)
    print("Version before:", x[2], "Version after:", replacement)
    try: 
      with open(filename, 'w') as file:
        file.write(data)
    except:
      print("Could not write to file")
      return "Failure"
  return "Success"
