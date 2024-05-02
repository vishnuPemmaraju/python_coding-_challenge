
class InvalidEmailError(Exception):
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        self.message = message
        print(self.message)

class NegativeSalaryError(Exception):
    def __init__(self, message="Invalid salary value. Salary should be non-negative."):
        self.message = message
        super().__init__(self.message)

class FileUploadError(Exception):
    def __init__(self, message="Error uploading file."):
        self.message = message
        super().__init__(self.message)

class DeadlineExceededError(Exception):
    def __init__(self, message="Application deadline exceeded."):
        self.message = message
        super().__init__(self.message)




