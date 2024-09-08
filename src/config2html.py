#config2html
import sys
cfg = sys.argv[1]

def parse_file_as_str(file0):
    F = open(file0,'r')
    str0 = F.read()
    F.close()
    return str0


def write_str_to_file_with_mode(str1,file1, mode, print_log=True):
    F = open(file1,mode)
    F.write(str1)
    F.close()
    if(print_log):
        if(mode =="w"):
            print ("created the file ", file1)
        elif (mode=="a"):
            print("appended to the file ", file1)
    return

def remove_comments(str1):
    strout = ""
    for line in str1.split("\n"):
        if(line[:2]!="//"):
            strout += line + "\n"
    return strout

def get_str_bw(str1, start, end, search_start=0,print_error=False):
    index_start = str1.find(start,search_start)
    index_end   = str1.find(end,index_start)
    str_return = str1[index_start+len(start):index_end]
    if((index_start == -1) or (index_end == -1)):
        if(print_error):
            print ("start : ",start)
            print ("end : ",end)

    if((str_return == "") or (index_start == -1) or (index_end == -1)):
        str_return = "-"

    return str_return,index_end

cfg_str = parse_file_as_str(cfg)
cfg_str_nocomments = remove_comments(cfg_str)
heading = get_str_bw(cfg_str_nocomments, "Heading :", "\n")[0].strip()

#print (heading)

questions = cfg_str_nocomments.split("/startq")[1:] #initial part will be headers
questions = [i.replace("/endq","").strip() for i in questions]
#print (questions)

html_out = '''<!DOCTYPE html><html lang="en">
<head>'''
#print (html_out)

num = 1
for q in questions:
    question = get_str_bw(q, "Q", "\nI")[0].strip()
    image = get_str_bw(q,"I","\nO")[0].strip()
    options = get_str_bw(q,"O","\nS")[0].strip()
    solution = get_str_bw(q,"\nS",q[-1])[0].strip()
    #print (question)
    #print (image)
    #print (options)
    #print (solution) #cmd + alt + down multiline like vim ctrl+v
    #html_out += '<h3>content</h3>'.replace("content", "Question"+str(num) )
    html_out += '<h2>content</h2>'.replace("content",  str(num)+". "+question)+"\n"
    if(image != ""):
        html_out += '<center><img src="imgpng" class="center" style="width:400px;height:400px;"></center>'.replace("imgpng", image)+"\n"
    if(options!= ""):
        html_out += '<p>content</p>'.replace("content", "Options "+options  )+"\n"
    html_out += '<p>content</p>'.replace("content", "Solution "+solution)+"\n"

    num += 1 

html_out += "</head></html>"+"\n"

print (html_out)
write_str_to_file_with_mode(html_out, cfg.replace(".txt",".html"), "w")