import os

class GradeManager:
    def __init__(self, filename="grades.txt"):
        self.filename = filename

    def add_default_students(self):
        students = [
            ("1001", "Alice Johnson", "Mathematics", "A"),
            ("1002", "Bob Smith", "Physics", "B+"),
            ("1003", "Charlie Brown", "Chemistry", "A-"),
            ("1004", "Daisy Miller", "English", "B"),
            ("1005", "Ethan Davis", "History", "A"),
        ]
        """Adds five default student records to the file."""
        # TODO: Implement logic to add default students to the file
        pass

    def view_grades(self):
        """Reads and returns student grades from the file."""
        # TODO: Implement logic to read and returns student grades
        pass

def main():
    manager = GradeManager()

    # TODO: Call function to add default students
    pass

    # TODO: Call function to display student grades
    pass

if __name__ == "__main__":
    main()
