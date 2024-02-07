# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 



def add(list, item):
  list.append(item)
  pass


def remove(list, index):
  del list[index] 
  pass


def clear(list):
  list.clear()
  pass


def print_list(list):
  if len(list) == 0:
    print("nothing to print")
    pass  
  print(list)
  pass


def show(list):
  print_list(list)
  pass

list = []
print("List is empty now, what you want to do?")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index"))
  if choice == 1:
    item = input("What you want to add?\n")
    if len(list) > 10:
      print("too much items in list")
    if len(item) > 100:
      print("too much symbols")
    elif len(item)<100: 
      add(list, item)
      print_list(list)
    elif len(item) <= 0:
      print("not enough symbols")
    
  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print_list(list)
  elif choice == 3:
    clear(list)
    print_list(list)
  elif choice == 4:
    print_list(list)
  elif choice == 5:
    show(list)
  else:
    print("Invalid input")
  
