# Here we'll talk about the novel and perhaps tantalizing concept 
# of slicing. Slicing is the process through which you can extract 
# some continuous part of a string. For example: string is "python"

bounded_by = input('Enter String : ')
tag_name = input('Enter tag : ')

size = len(bounded_by)
i = int(size/2)
ans = bounded_by[:-i] + tag_name + bounded_by[-i:]

print(ans)