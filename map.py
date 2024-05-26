
# key = always string
# value = any type

a = {
    "101": "ram",
    "102": "ravi"
}

print(a)    
print(a["101"])
print(a.get("101"))
print("102" in a)
print("x" in a)
print(len(a))

a["103"] = "somu"
print(a)

print([x for x in a.keys()])
print(a.values())
print(a.items())

a.pop("101")
print(a)

# a.clear()
# print(a)

# format string
print   ('--format string--')
print("iterating using key")
for key in a:
    print(f"key is {key} and value is {a[key]}")
    # "key is " + str(key) + "and value is " str(a[key])

for key, value in a.items():
    print(f"{key},{value}")