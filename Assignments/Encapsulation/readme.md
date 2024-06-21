# Encapsulation in Python
# Basics of Encapsulation
# Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit called a class. Encapsulation also restricts direct access to some of an object's components, which is a means of preventing accidental or unauthorized modification of data. This is typically done using access modifiers:

# Public: Accessible from anywhere.
# Protected: Accessible within the class and its subclasses (conventionally denoted with a single underscore _).
# Private: Accessible only within the class itself (denoted with double underscores __).
# Real-Life Example
# Consider a real-life scenario of a bank account. A bank account has a balance, and you can perform operations such as deposit and withdraw. However, you shouldn't be able to directly modify the balance without using these operations. Encapsulation helps in achieving this control.

# code Explanation:
# The __balance attribute is private, meaning it cannot be accessed directly from outside the class.The deposit and withdraw methods provide controlled access to modify the balance. The get_balance method allows viewing the balance without modifying it.
