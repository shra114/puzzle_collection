from tinyhtml import html, h  
    
html_content = html(lang="en")(  
    h("head")(  
        (h("h1")("hello Learners!!")),  
    ),  
).render()  
print(html_content)  