# Day 11
# Problem 11
# Date 21 Feb 2021
# Time 7:00 PM

stringSet = ['dog', 'deer', 'deal']


def autoComplete(string, stringSet):
    return [s for s in stringSet if s.startswith(string)]


print(autoComplete('de', stringSet))
