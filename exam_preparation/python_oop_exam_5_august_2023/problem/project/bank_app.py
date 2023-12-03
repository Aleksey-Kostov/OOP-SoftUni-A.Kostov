from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPES_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_TYPES_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPES_LOANS:
            raise Exception("Invalid loan type!")
        self.loans.append(self.VALID_TYPES_LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPES_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        valid_types = self.VALID_TYPES_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(valid_types)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_clients_with_client_id(client_id)
        loan = self.find_loans_types(loan_type)
        if not client.POSSIBLE_LOANS_TYPES == loan_type:
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_clients_with_client_id(client_id)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loan = []
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                filtered_loan.append(loan)
        return f"Successfully changed {len(filtered_loan)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = []
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number.append(client)
        return f"Number of clients affected: {len(changed_client_rates_number)}."

    def get_statistics(self):
        total_clients_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_sum = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients)\
            if self.clients else 0

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_clients_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {granted_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""

    def find_clients_with_client_id(self, client_id):
        return next((c for c in self.clients if c.client_id == client_id), None)

    def find_loans_types(self, loan_type: str):
        return next((t for t in self.loans if t.__class__.__name__ == loan_type), None)
