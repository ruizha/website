from flask import Flask, render_template

app = Flask(__name__)

class NavbarItem:
    def __init__(self, name, text, active=False):
        self.name = name
        self.text = text
        self.active = active

class NavbarItemCollection:
    def __init__(self, items):
        self.item_order = [it.name for it in items]
        self.items = {}
        for it in items:
            self.items[it.name] = it
            if it.active:
                self.curr_active = it.name
        self.curr_active = None
    def set_active(self, name=None):
        if name == None or name == '': # if no active tab is specified, set all to inactive
            self.curr_active = None
        if name in self.items: 
            if self.curr_active != None:
                self.items[self.curr_active].active = False
            self.items[name].active = True
            self.curr_active = name

    def get_tabs(self):
        return [self.items[name] for name in self.item_order]

class Skill:
    def __init__(self, name, text, rating):
        self.name = name
        self.text = text
        self.rating = rating

navbar_items = [
    NavbarItem("home", "Home"),
    NavbarItem("projects", "Projects"),
    NavbarItem("contact", "Contact Me")
]

navbar_collection = NavbarItemCollection(navbar_items)
prog_skills = [
    Skill('python', "Python", 5),
    Skill("javascript", "JavaScript", 5),
    Skill("java", "Java", 5),
    Skill('kotlin', 'Kotlin', 4),
    Skill('c', "C", 4),
    Skill('cpp', 'C++', 3),
    Skill('sql', 'SQL', 4)
]

framework_skills = [
    Skill("flask", "Flask", 5),
    Skill("rxjava", "RxJava", 5),
    Skill("android", "Android", 5),
    Skill("nodejs", "Node.js", 4),
    Skill("expressjs", "Express.js", 4),
    Skill("mysql", "MySQL/MariaDB", 5),
    Skill("nginx", "Nginx", 3),
    Skill("docker", "Docker", 3)
]

@app.route("/")
def main():
    navbar_collection.set_active("home")
    return render_template("main.html", navbarItems=navbar_collection.get_tabs(), progSkills=prog_skills+framework_skills)

app.run(debug=True, port=3000)
