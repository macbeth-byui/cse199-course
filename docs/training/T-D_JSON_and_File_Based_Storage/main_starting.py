def add(bucket_list):
    activity = input("What do you want to add to your bucket list? ")
    year = int(input("What year do you want to do this? "))
    item = {"activity"  : activity,
            "year"      : year,
            "completed" : False}
    bucket_list.append(item)

def show(bucket_list):
    for i, item in enumerate(bucket_list):
        mark = "*" if item["completed"] else " "
        print(f"{i+1}. [{mark}] - {item["activity"].title()} ({item["year"]})")

def complete(bucket_list):
    show(bucket_list)
    choice = int(input("Mark which item complete? "))
    bucket_list[choice-1]["completed"] = True

def load():
    pass

def save(bucket_list):
    pass

def main():
    print("Welcome to your bucket list!")
    bucket_list = []
    choice = None
    while choice != "E":
        choice = input("\n(A)dd (S)how (C)omplete (E)xit > ")
        match choice.upper():
            case "A" : add(bucket_list)
            case "S" : show(bucket_list)
            case "C" : complete(bucket_list)

if __name__ == "__main__":
    main()
