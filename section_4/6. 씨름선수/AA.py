import sys


sys.stdin = open('in5.txt', 'rt')
n = int(input())

people = []


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def is_better(self, cmp_height, cmp_weight) -> bool:
        if self.height > cmp_height or self.weight > cmp_weight:
            return True

        return False


for i in range(n):
    pp = list(map(int, input().split()))
    people.append(Person(pp[0], pp[1]))

sorted_people = sorted(people, key=lambda x: x.height, reverse=True)

prev = 0
counter = 1

for i in range(1, n):
    if sorted_people[i].is_better(sorted_people[prev].height, sorted_people[prev].weight):
        counter = counter + 1
        prev = i

print(counter)

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
