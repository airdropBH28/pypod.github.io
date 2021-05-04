import os
import re
with open('index.html', 'r') as f:
    text = f.read()
    if 'iitm_logo' not in text:
        text = text.replace('<head>', '''<head>\n<link rel="icon" type="image/png" href="assets/images/iitm_logo.png">''')
    text = re.sub(r'(<title>)(.*?)(</title>)', r'\1Python Home\3', text)

with open('index.html', 'w') as f:
    f.write(text)
 
with open('404.html', 'r') as f:
    text = f.read()
    if 'iitm_logo' not in text:
        text = text.replace('<head>', '''<head>\n<link rel="icon" type="image/png" href="assets/images/iitm_logo.png">''')
    text = re.sub(r'(<title>)(.*?)(</title>)', r'\1Python 404\3', text)

with open('404.html', 'w') as f:
    f.write(text)
 

chapters = [chapter for chapter in os.listdir('.') if 'chapter' in chapter]

for chapter in chapters:
    lessons = os.listdir(chapter)
    for lesson in lessons:
        lesson_path = os.path.join(chapter, lesson)
        with open(lesson_path, 'r') as f:
            text = f.read()
            if 'iitm_logo' not in text:
                text = text.replace('<head>', '''<head>\n<link rel="icon" type="image/png" href="../assets/images/iitm_logo.png">''')
            lesson_name = lesson.split('.html')[0].capitalize()
            text = re.sub(r'(<title>)(.*?)(</title>)', rf'\1{lesson_name}\3', text)
        
        with open(lesson_path, 'w') as f:
            f.write(text)

