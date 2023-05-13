def base64_encode(input_string):
    # Defino tabelen per Base64
    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
 
    # Konverto input string-un ne nje varg te bajtave
    input_bytes = input_string.encode()
 
    # Inicializo output stringun 
    output_string = ""
 
    # Kalo me loop neper secilin input (vargun e bajtave) procesoji 3 bytes ne te njejten kohe 
    for i in range(0, len(input_bytes), 3):
        # Merri 3 bytes per proces 
        byte1 = input_bytes[i]
        byte2 = input_bytes[i+1] if i+1 < len(input_bytes) else 0
        byte3 = input_bytes[i+2] if i+2 < len(input_bytes) else 0
        
        value1 = byte1 >> 2
        value2 = ((byte1 & 0x03) << 4) | (byte2 >> 4)
        value3 = ((byte2 & 0x0F) << 2) | (byte3 >> 6)
        value4 = byte3 & 0x3F
 
        # Shiko karakterin korespondues per secilen vlere te karakterit te Base64
        char1 = b64_table[value1]
        char2 = b64_table[value2]
        char3 = b64_table[value3]
        char4 = b64_table[value4]
        # Shfaqi 4 karakteret e output-it te Base64
        output_string += char1 + char2 + char3 + char4
 
    padding_length = 4 - (len(input_bytes) % 3)
    output_string += '=' * padding_length
 
    #  Ktheje rezultatin
    return output_string

 # Write the Base64-encoded string to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_string)

def base64_decode_file(input_file_path, output_file_path):
    # Define the Base64 decoding table
    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Convert the four values to three bytes

        byte1 = (value1 << 2) | (value2 >> 4)

        byte2 = ((value2 & 0x0F) << 4) | (value3 >> 2)

        byte3 = ((value3 & 0x03) << 6) | value4

        # Add the three bytes to the output byte array

        output_bytes += bytes([byte1, byte2, byte3])

    # Write the decoded byte array to the output file

    with open(output_file_path, 'wb') as output_file:

        output_file.write(output_bytes)

 

def main(args):

   

    if (args.mode == 'encode' or args.mode == 'e'):

        base64_encode_file(args.inputfilename, args.outputfilename)

    else:

        base64_decode_file(args.inputfilename, args.outputfilename)

    return

if __name__ == '__main__':



    parser = argparse.ArgumentParser(description='Base64')

    required = parser.add_argument_group('required arguments')

    required.add_argument('-m', '--mode', choices=['encode', 'e', 'decode', 'd'],

                          help='Mode: encode or decode', required=True, dest='mode')



    required.add_argument("-i", "--inputfilename",

                          help="Input file to be processed", required=True, dest='inputfilename')



    required.add_argument("-o", "--outputfilename",

                          help="Output file to be created", required=True, dest='outputfilename')



    main(parser.parse_args())