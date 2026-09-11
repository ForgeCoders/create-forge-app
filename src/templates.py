def list_templates():
  return [
    "Python",
    "HTML/CSS/JavaScript",
    "Node.js",
    "React"
  ]

def display_templates():
  templates = list_templates()
  for index, template in enumerate(templates, start=1):
    print(f"{index}. {template}")

def select_template():
  templates = list_templates()
  display_templates()

  while True:
    choice = input("Enter the number of the template you want: ")

    if not choice.isdigit():
      print("Please enter a valid number.\n")
      continue

    choice = int(choice)

    if choice < 1 or choice > len(templates):
      print(f"Please select a number between 1 and {len(templates)}.\n")
      continue

    return templates[choice - 1]