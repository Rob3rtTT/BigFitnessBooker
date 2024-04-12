from booker import Booker
import sys

if __name__ == "__main__":
    _class_booker = Booker()
    if sys.argv[1] == "--getallclasses":
        print(_class_booker.classes)
    if sys.argv[1] == "--bookclass":
        class_id = sys.argv[2]
        class_name = _class_booker.class_name(class_id)  # Call the property with the class_id argument
        print(f"You have booked a class for {class_name}")
