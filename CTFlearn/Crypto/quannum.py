import binascii

def read_data(file):
    with open(file, "r") as input_file:
        data = input_file.readline()
        return data

def get_agreed_bytes(data_sent, bases_measured, bases_correct):
    agreed_bits = []
    i=0
    for i in range(len(str(bases_correct))):
        if bases_correct[i] == 'v':
            if bases_measured[i] == '+':
                if data_sent[i] == '-':
                    agreed_bits.append(0)
                else:
                    agreed_bits.append(1)
            else:
                if data_sent[i] == '/':
                    agreed_bits.append(0)
                else:
                    agreed_bits.append(1)
   # return hex(int("".join([str(c) for c in agreed_bits]), 2))[2:-1]
    return ''.join([str(c) for c in agreed_bits]) 

def main():
    data_sent = read_data("transmission1.txt")
    bases_measured = read_data("transmission2.txt")
    bases_correct = read_data("transmission3.txt")
    data = get_agreed_bytes(data_sent, bases_measured, bases_correct)

#main()
text = 'Simply Easy Learning'

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print ("**Binary to Ascii** \n")
print (data_b2a)
