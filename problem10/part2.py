#with open('problem10_input.txt') as file:
with open('problem10_input.txt') as file:
    jolts = file.read().splitlines()

nums = [int(i) for i in jolts]

top = max(nums) + 3
nums = set(nums)
nums.add(top)
a, b, c = 0, 0, 1
for i in range(1, top + 1):
    if i in nums:
        a, b, c = b, c, a + b + c
    else:
        a, b, c = b, c, 0
print(c)