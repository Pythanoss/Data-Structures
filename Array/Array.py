#Animals array is created
Animals = ['Cat','Dog','Fox','Lion']

#Array printing function
def show():
    print("Arrya Contents:----")
    for animal in Animals:
        print(animal)

#printing array
show()

#Adding animal in Animals array
Animals.append('Tiger')
print("\nTiger is added")
show()