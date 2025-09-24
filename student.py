class Student: 
    def __init__(self, roll_number,name, marks):
        self.name = name 
        self.roll_number = roll_number 
        self.marks = marks # Dict of marks of different subjects 

    def calculate_total_marks(self):
        return sum(self.marks.values())
    
    def calculate_average(self):
        return self.calculate_total_marks()/len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average() 
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"
    def to_dict(self):
        return {
            "roll_no" : self.roll_number,
            "name" : self.name ,
            "marks" : self.marks ,
            "total" : self.calculate_total_marks() ,
            "average" : self.calculate_average() ,
            "grade" : self.calculate_grade() 
        }

