def to_upper_case(input_file, output_file):
    input_file = open('input_file.txt','r')
    inputString = str(input_file.read()).upper()
    print(inputString)
    open('output_file.txt','a')
    output_file.write(inputString)
    output_file.close()
    input_file.close()

input_file = open('input_file.txt','w')
input_file.write("Hello world")
input_file.close()#remember this!!!
output_file = open('output_file.txt','w')
print(to_upper_case(input_file,output_file))