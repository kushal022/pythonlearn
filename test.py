# make a program to calculate total expenses Take input number of products
book = input("Enter book price:")
notebook = input("Enter notebook price:")
pen = input("Enter pen price:")
pencil = input("Enter pencil price:")
marker = input("Enter marker price:")

book = int(book)
notebook = int(notebook)
pen = int(pen)
pencil = int(pencil)
marker = int(marker)

TotalExpense = book+notebook+pen+pencil+marker
print("Total Expense:",TotalExpense)
