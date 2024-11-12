# Coffee Machine Simulator

This project is a Python-based coffee machine simulator that allows users to interact with a machine capable of making three different types of drinks (Espresso, Latte, and Cappuccino). The system simulates resource management (water, milk, and coffee), payment processing, and drink preparation based on available resources.

## Description

The program allows the user to select a drink from the menu, make the payment, and prepare the selected drink if enough resources are available. As drinks are prepared, resources are consumed, and the system will notify the user if there are enough resources to prepare the selected drink.

### Key Concepts and Techniques:
  
1. **Object-Oriented Programming (OOP)**:
   The project is built using Object-Oriented Programming (OOP) principles. This allows for better code organization, reusability, and maintainability. Key OOP concepts applied in the project include:
   
   - **Classes and Objects**: The program models real-world objects like a `CoffeeMaker`, `Resources`, `MenuItem`, and `MoneyMachine`. Each of these entities is represented by a class, which defines their attributes and behaviors (methods). For example, the `CoffeeMaker` class manages coffee preparation, while the `MoneyMachine` class handles payment processing.
   
   - **Encapsulation**: Each class encapsulates its own data and behavior. For example, the `Resources` class holds information about available resources like water, milk, and coffee, while the `CoffeeMaker` class has methods to interact with those resources and perform actions like checking if resources are sufficient or deducting amounts when a drink is made.
   
   - **Abstraction**: Complex processes, such as managing resources and payments, are abstracted into well-defined methods that hide the underlying logic. Users of the classes don't need to know how resources are managed or how the payment process works internally—they simply interact with simple methods like `make_payment()` or `make_coffee()`.

2. **Data Structures**:
   - **Lists**: A list (`resources_list`) is used to store instances of resources like water, milk, and coffee. This allows the system to easily iterate through the available resources and perform checks or deductions.
   - **Dictionaries**: The `MenuItem` class uses a dictionary to store the ingredients and their required amounts for each drink. This allows quick lookup and easy management of drink recipes.
  
3. **Control Flow**:
   The program uses loops (`while` loop) and conditionals (`if`, `else`) to control the flow of the application:
   - The main loop continues to run until the user selects the "off" option.
   - The program checks if there are enough resources before allowing the user to make a purchase.
   - After successful payment, the appropriate resources are deducted, and the drink is prepared.
---

In summary, this project leverages basic and powerful OOP principles such as classes, encapsulation, and abstraction to create a simple, yet extendable coffee machine simulation. The combination of Python's simplicity and OOP's power allows for a clean, understandable, and maintainable codebase.
