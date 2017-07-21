import shlex, subprocess
import os
import re


base_path = 'C:\\Unnamed\\'
dirs = [os.path.join(base_path, 'dir'+str(x)) for x in range(29) ][1:29]
seps = [r'\.', r'\\', r'-',r'/',r' ']
sep = r'[\.\-/ ]'
date = [r'\b(((0[13578]|(10|12))', r'(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)', 
    r'(0[1-9]|[1-2][0-9]|30)))', 
    r'(199\d{1}|20[01]\d{1})']
month_date = [r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)', 
    r'((199\d{1}|20[01]\d{1})|((((0[1-9]|[1-2][0-9]|3[0-1]))|(02', r'(0[1-9]|[1-2][0-9]))|((0[469]|11)', 
    r'(0[1-9]|[1-2][0-9]|30)))', 
    r'(199\d{1}|20[01]\d{1})))']
year_date = r'\b(199\d{1}|20[01]\d{1})'
patterns =  [(x, x.join(month_date)) for x in seps] + [(x,x.join(date)) for x in seps] + [('+',year_date)]



for d in dirs:

    if (os.path.isdir(os.path.join(d, 'ocr-pdfs'))): 
        pdf_files = [os.path.join(d, 'ocr-pdfs', f) for f in os.listdir(os.path.join(d, 'ocr-pdfs')) if f.endswith("ocr.pdf")]

        for f in pdf_files:
            outfile = '.'.join([f.rsplit('-',1)[0],'txt'])
            if not os.path.isfile(outfile):
                print(outfile)
                args = ['pdftotext' , f , outfile]
                subprocess.call(args)
            #os.unlink(f)




        files = [os.path.join(d, 'ocr-pdfs', f) for f in os.listdir(os.path.join(d, 'ocr-pdfs')) if f.endswith(".txt")]
        print('\n'.join(map(str, files[:20])))
        print(d, len(files))
        datefile = open(d + '.csv', 'w+')

        
        for f in files:
            try:
                try:
                    with open(f, 'r', encoding="utf8") as file:
                        lines = file.readlines()
                except UnicodeDecodeError as err:
                    with open(f, 'r') as file:
                        lines = file.readlines()
                        print(err)
                        pass
            except:
                print(err)
                pass
                
            matches = []
            
            for pattern_type, pattern in patterns:
                matches.append(pattern_type)

                for line in lines:
                    try:
                        match = re.search(pattern, line)
                    except TypeError as err:
                        print(pattern)
                        raise
                    if match:
                        matches.append(match.group(0))
                if (matches[-1] if len(matches) else None) != '?':
                    matches.append('?')
            if len(matches):
                print(','.join(['.'.join([f.rsplit('.',1)[0], 'pdf'])] + matches), file=datefile)
            else:
                print('.'.join([f.rsplit('.',1)[0], 'pdf']) + ',NO DATES', file=datefile)
                pass



        datefile.close()