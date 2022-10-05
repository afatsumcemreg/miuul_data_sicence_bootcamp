salaries = [100, 200]
nlis = []

for salary in salaries:
    if salary > 100:
        salary = salary * 0.2 + salary
        nlis.append(salary)
    else:
        nlis.append(salary)
print(nlis)

nums = range(10)
{n: n**2 for n in nums if n % 2 == 0}