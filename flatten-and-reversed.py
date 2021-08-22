
x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
y = [[1, 2], [3, 4], [5, 6, 7]]


lst_x = []
lst_y = []

def flatten(a, container):
    for item in a:
        if isinstance(item, list):
            flatten(item, container)
        else:
            container.append(item)
    return container



def reverse(a,container):
    a.reverse() 
    for item in a:
        if isinstance(item,list):
            item.reverse()
            container.append(item)
        else:
            reverse(item,container)
    return container


print(f"\nOriginal array: {x}")
flatten(x,lst_x)
print(f"Flatten array: {lst_x}\n")


print(f"Original array: {y}")
reverse(y,lst_y)
print(f"Reversed array: {lst_y}")