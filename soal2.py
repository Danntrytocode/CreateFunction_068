#Use the lambda function to create a function that calculates the area of a circle!
#Input is the length from the center of the circle to the border (jari-jari lingkaran).
area_lingkaran = lambda r : 3.14 * r**2

input_jari2 = float(input("Masukkan jari-jari lingkaran (dalam cm): "))
print(f"Luas lingkaran dengan jari-jari {input_jari2}cm adalah: {area_lingkaran(input_jari2)}cm^2")