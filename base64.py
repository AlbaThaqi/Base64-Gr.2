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
