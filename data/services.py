from .models import userprofile, get_user_model

def transcript_extractor():
    import pdfplumber
    import re
    import json
    
    def is_float(element) -> bool:
        if not '.' in element:
            return False
        return element.replace('.','',1).isdigit()

    #insert transcript file path here
    path = 'example.pdf'

    full_text = ''
    student = {}
    quarters = []

    with pdfplumber.open(path) as pdf:
        for  page  in pdf.pages:
            full_text += page.within_bbox((0, 100, 400, 600), relative=False).extract_text(layout=True)
            full_text += page.within_bbox((400, 100, 792, 600), relative=False).extract_text(layout=True)
            
    full_text = full_text[full_text.index('Beginning of Academic Record'):]

    for match in re.finditer(r'\d{4}-\d{4}', full_text):
        year = match.group()
        season = full_text[match.end() + 1: full_text.index(" ", match.end() + 1)].strip()
        season_start = full_text.index("Grade", match.end() + 1) + 9
        season_end = full_text.index("UG Term", season_start)
        season_text = full_text[season_start: season_end]
        season_tokens = season_text.split(" ")
        quarter = {}
        quarter['quarter'] = season
        quarter['year'] = year
        courses = []
        course = {}
        title = ''
        lecturer = ''
        throwaway = False
        print(season_tokens)
        for t in season_tokens:
            if (t != ''):
                if (throwaway and '\n' in t):
                    throwaway = False
                    continue
                if (throwaway):
                    continue
                if (not 'subject' in course and t.isupper()):
                    course['subject'] = t
                    continue
                if (not 'subject' in course):
                    continue
                if (not 'number' in course):
                    course['number'] = t
                    continue
                if (not 'type' in course):
                    course['type'] = t
                    continue
                if (not 'title' in course and not is_float(t)):
                    title += t + " "
                    continue
                if (not 'title' in course and is_float(t)):
                    course['title'] = title + " "
                    course['units_attempted'] = t
                    continue
                if (not 'units_earned' in course):
                    course['units_earned'] = t
                    continue
                if (not 'grade' in course):
                    course['grade'] = t.strip()
                    continue
                if (t.isupper()):
                    title += t + " "
                    continue
                if (t == "Previous"):
                    throwaway = True
                    continue
                if (not 'lecturer' in course and not '\n' in t):
                    lecturer += t + " "
                    continue
                if (not 'lecturer' in course):
                    lecturer += t.strip()
                    course['lecturer'] = lecturer
                    course['title'] = title.strip()
                    courses.append(course)
                    course = {}
                    title = ''
                    lecturer = ''
                    continue
                
            
        quarter['courses'] = courses
        quarters.append(quarter)
        
    student['quarters'] = quarters   
    print(student)