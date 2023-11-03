class Task:
    comments = []
    completed = False

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if new_name != self.name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same."

    @staticmethod
    def add_comment(comment: str):
        Task.comments.append(comment)

    @staticmethod
    def edit_comment(comment_number: int, new_comment: str):
        for index in range(len(Task.comments)):
            if index == comment_number:
                Task.comments[index] = new_comment
                return ", ".join(Task.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
