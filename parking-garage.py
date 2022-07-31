class ParkingGarage():
    '''
        Parking Garage Class to mimic a parking garage and spaces available.

        Expected values for attributes:
        -tickets: expected as a list
        -parkingSpaces: expected as a list
        -currentTicket: expected as a dictionary
    '''

    # initialze the ParkingGarage with empty tickets and parkingSpaces lists, 
    #  and currentTicket's 'paid' value to be False (ticket not paid yet)
    def __init__(self, tickets = [], parkingSpaces = [], currentTicket = {'paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()

    def payForParking(self):
        payment = int(input("Enter an amount to pay for the ticket: "))
        if payment > 0:
            print("Your ticket has been paid. You have 15 minutes to leave the garage.")
            self.currentTicket['paid'] = True
        else:
            print("Please enter a correct payment amount!")

    def leaveGarage(self):
        if self.currentTicket['paid']:
            print("Thank you, have a nice day!")
            self.parkingSpaces.append(len(self.parkingSpaces) + 1)
            self.tickets.append(len(self.tickets) + 1)
        else:
            payment = int(input("Enter an amount to pay for the ticket: "))
            if payment > 0:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(len(self.parkingSpaces) + 1)
                self.tickets.append(len(self.tickets) + 1)
            else:
                print("Please enter a correct payment amount!")


# Testing class and methods:

# Create a ParkingGarage instance and verify that attributes initialized correctly (10 tickets and 10 parking spaces)
my_garage = ParkingGarage(list(range(1,11)), list(range(1,11)))
print("Initial tickets and parking spaces:")
print(my_garage.tickets)
print(my_garage.parkingSpaces)

# Take a ticket and verify that tickets and parkingSpaces attributes updated correctly (9 tickets and 9 parking spaces)
my_garage.takeTicket()
print("\nUpdated tickets and parking spaces after taking a ticket: ")
print(my_garage.tickets)
print(my_garage.parkingSpaces)

# Check that leaving garage with unpaid ticket prompts user to pay, then check that tickets and parkingSpaces updated (10 each)
print("\nUnpaid ticket and leaving garage: ")
my_garage.leaveGarage()
print(my_garage.tickets)
print(my_garage.parkingSpaces)

# Check that paying for parking updates the currentTicket dictionary from False to True
# First update value of currentTicket to not be paid (False)
my_garage.currentTicket['paid'] = False
print("\nPaying for parking: ")
print(my_garage.currentTicket)
my_garage.payForParking()
print(my_garage.currentTicket)

# Check that leaving garage with paid ticket works, and updates parkingSpaces and tickets appropriately (up to 11 each, assuming user paid each time prompted)
print("\nPaid ticket and leaving garage: ")
my_garage.leaveGarage()
print(my_garage.tickets)
print(my_garage.parkingSpaces)

