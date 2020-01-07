#Day 5 #Task 1
oldest = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
x = [name for name, number in oldest.items() if number == 71]
print(x)
#"Emma"


oldest = {
  "Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33
}
x = [name for name, number in oldest.items() if number == 48]
print(x)
#"Sam"