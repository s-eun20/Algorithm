take = []
people = 0

for _ in range(4):
    out_people, take_people = map(int, input().split())
    people +=take_people
    people -= out_people
    take.append(people)

print(max(take))