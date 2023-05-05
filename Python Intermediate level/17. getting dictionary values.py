courses = {
    "js": "JavaScript",
    "python": ["Python 1", "Python 2"],
    "html": "HTML 1"
}

# print(courses.get("css", "css 2"))
if courses.get("css", None):
    print("You are enrolled in css")