# Book Store

# Dictionary of books and prices
book_prices = {
  "Harry Potter": 13.54,
  "The Hobbit": 12.50,
  "Percy Jackson": 10.99,
  "The Hungar Games": 14.99
}

# List to store the customer's books
shopping_cart = []

print("Welcome to the Book Store!!!")
print("Available books:")

for book in book_prices:
  print(book)

print("\nEnter 2 books you would like to buy:")

for i in range(2):
  book = input()
  shopping_cart.append(book)

total = 0

print("\nYour Receipt:")

for book in shopping_cart:
  if book in book_prices:
    print(f"{book}: ${book_prices[book]:.2f}")
    total += book_prices[book]
  else:
    print(f"{book}: Not available")

print(f"\nTotal: ${total:.2f}")
    
