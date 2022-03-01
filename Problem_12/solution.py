# Day 12
# Problem 12
# Date 21 Feb 2022
# Time 7:05 PM

def get_steps(n, step_sizes):
    stepSets = list()

    if n < min(step_sizes):
        return stepSets

    for step_size in step_sizes:
        if n == step_size:
            stepSets.append([step_size])
        elif n > step_size:
            child_stepSets = get_steps(n - step_size, step_sizes)
            for i in child_stepSets:
                stepSets.append([step_size] + i)
    return stepSets


print(len(get_steps(4, [1, 2])))
print(get_steps(4, [1, 2]))
