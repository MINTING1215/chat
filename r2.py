def read_file(filename):
    lines = []
    with open(filename,'r', encoding = 'utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    mindy_sticker_count = 0
    minting_sticker_count = 0
    mindy_image_count = 0
    minting_image_count = 0
    mindy_word_count = 0
    minting_word_count = 0
    for line in lines:
        s = line.split(' ')
        time =s[0]
        name =s[1]
        if name == 'Mindy':
            if s[2]== '貼圖':
                mindy_sticker_count += 1
            elif s[2] == '圖片':
                mindy_image_count += 1
            else:
                for m in s[2:]:
                    mindy_word_count += len(m)
        elif name == 'minting': 
            if s[2]=='貼圖':
                minting_sticker_count += 1
            elif s[2]== '圖片':
                minting_image_count += 1
            else:
                for m in s[2:]:  
                    minting_word_count += len(m)
    print('Mindy說了', mindy_word_count,'個字')
    print('Mindy傳了', mindy_sticker_count, '個貼圖')
    print('Mindy傳了', mindy_image_count, '張圖片')
    print('minting說了', minting_word_count, '個字')
    print('minting傳了', minting_sticker_count, '個貼圖')
    print('minting傳了', minting_image_count, '張圖片')

def write_file(filename,lines):
	with open (filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')


def main():
    lines = read_file('[LINE]Mindy.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)

main()
