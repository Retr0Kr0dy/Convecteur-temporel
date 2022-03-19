import sys

def main():  
    try:
        t1 = sys.argv[1]
        t2 = sys.argv[2]
        t3 = sys.argv[3]
    except:
        print('\n' + '\x1b[1;31;40m' + '[!]' + '\x1b[0m' + '\x1b[1;33;40m' +" Error - Bad usage" + '\x1b[0m' + "\n" + '\x1b[3;33;40m' + "   | use help arguments\n      | Usage : <script-name>.py <value-to-convert> <input-base> <output-base>\n\n<value to convert> can't contain spaces\n<input-base> starting base (ex: 2, 10, 16)\n<output-base> end base (ex: 2, 10, 16)" + '\x1b[0m' + "\n") 
        exit(-1)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯´≡±‗¾¶§÷¸°¨·¹³²■'    
    def con(Num, input_base, output_base):
        stack = []
        Num = int(Num, int(input_base))
        while Num > 0:
            stacker = Num % output_base
            stack.append(stacker)
            Num = Num // output_base
        form = []
        while stack:
            form.append(alphabet[stack.pop()])
        return ''.join(form)
    result = con(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    answer = '\n' + '\x1b[1;34;40m' + '[!]' + '\x1b[0m' + '\x1b[3;33;40m' + f"{t1} in base {t2} ==> {result} in base {t3}" + '\x1b[0m'
    print (result)
if __name__ == '__main__':
    main()