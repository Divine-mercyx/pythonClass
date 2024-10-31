first = int(input("enter a number: "))
second = int(input("enter a number: "))
third = int(input("enter a number: "))


if first > second and second > third:
    print(f"{third} {second} {first}")

	
elif second > first and first > third:
    print(f"{third} {first} {second}");


elif third > second and second > first:
    print(f"{first} {second} {third}")


elif first > third and third > second:
    print(f"{second} {third} {first}")


elif second > third and third > first:
    print(f"{first} {third} {second}")


elif third > first and first > second:
    print(f"{second} {first} {third}")