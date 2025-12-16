# Training D - JSON and File Based Storage

## Background

* If we don't save data (e.g. file, database), then when we exit, all information is lost because memory is cleared.

* How we can store data into a file:

  * Write data in `CSV` (Comma Separated Value) format with each row representing a record
  * Write data in a formatted `JSON` (Javascript Object Notation) or `XML` (Extended Markup Language).
  * Write data (frequently configuration data) in `TOML` (Tom's Obvious, Minimal Language) or `YAML` (YAML Ain't Markup Language)
  * Write data in binary format (compressed space) using libraries like `pickle`

* The `JSON` format is considered human-readable and is commonly used to store and transfer information.

* We can represent a `dictionary` (or `hashmap`) in JSON using curly braces, colons, and commas:

```json
{
    "temp": 67,
    "sky": "cloudy",
    "pressure": 1021.67
}
```

* We can represent a list of records by using a `list` of `dictionary` objects.  The list is represented with square brackets and commas:

```json
[
    {
        "temp": 67,
        "sky": "cloudy",
        "pressure": 1021.67
    },
    {
        "temp": 54,
        "sky": "rain",
        "pressure": 1020.67
    },
    {
        "temp": 71,
        "sky": "sunny",
        "pressure": 1023.67
    }
}
```

## Example

1. Copy the following code into a file called `main.py`:

```python
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
```

1. Run the program and observe how it works and how it does not save data after you exit.

1. Implement the `save` function.  You will need to import the `json` package.  Format the JSON data so it has a 4 space indentation.  Call the `save` function after any modification of the the `bucket_list` (list of dictionaries).

1. Run the program and add a bucket list item.  Open the `bucket.json` file when it is created.  Keep adding items and marking some of them complete.  Observe how `bucket.json` changes and is "human-readable".

1. Implement the `load` function.  Include a `try` and `except` block in case the file does not exist.  If the file does not exist, return an empty list.  Otherwise, read the JSON data and convert it a list of dictionaries again.

1. Run the program again.  Add some bucket list items.  Exit the program and restart.  Notice that the bucket list is populated again.

## Discussion

Where might you use a JSON file in one of your projects?

## Solution

* [main.py](main.py)
