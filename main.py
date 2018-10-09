from flask import Flask, render_template
import random

app = Flask(__name__)
DEBUG = False
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
    NavbarItem("work", "Where I Worked"),
    NavbarItem("projects", "Projects"),
    NavbarItem("contact", "More About Me")
]

navbar_collection = NavbarItemCollection(navbar_items)

languages = [
    Skill('python', "Python", 5),
    Skill("javascript", "JavaScript", 5),
    Skill("java", "Java", 5),
    Skill('kotlin', 'Kotlin', 4),
    Skill('c', "C/C++", 4),
    Skill('sql', 'SQL', 4),
    Skill('html', 'HTML', 5),
    Skill('css', 'CSS', 4),
]

frameworks = [
    Skill("flask", "Flask", 5),
    Skill("django", "Django", 4),
    Skill("rxjava", "RxJava", 4),
    Skill("android", "Android", 4),
    Skill("nodejs", "Node.js", 4),
    Skill("expressjs", "Express.js", 4),
    Skill("nginx", "Nginx", 3),
    Skill("docker", "Docker", 3),
]

tools = [
    Skill('linux', 'Linux', 4),
    Skill('git', 'Git', 4),
    Skill('vim', 'Vim', 5),
    Skill('digitalocean', 'DigitalOcean', 3),
]

lfj_subtitles = [
    'Looking for job',
    '"...a fine choice" ~ everyone',
    '<span><a class=\'text-link\' href="https://www.dropbox.com/s/nvtbp6si16ng24b/rui_zhang_resume.pdf?dl=1" style="text-decoration: none;">Here\'s my resume</a></span>',
    'Graduating this semester',
    'Are you a recruiter?',
    'Coder for hire'
]

working_subtitles = [
    'Working at a Cool Place',
    'I Am Taken',
    'Enjoying my Time',
    'Currently Bug Slaying',
    'Employed'
]

subtitles = [
    'Trader of Memes',
    'Bug Slayer',
    'Code Slinger',
    'Spittin\' Hot Lines',
    'Vim and Emacs are both good',
    'Preventing Segfaults'
]

class SubtitleDistribution:
    def __init__(self, subtitles):
        self.distribution = {subtitle: 0 for subtitle in subtitles}

    def get_subtitle(self):
        total = sum(self.distribution.values()) + 1
        inverted = {k: total - v for k,v in self.distribution.items()}
        choices = []
        for k,v in inverted.items():
            choices += [k] * v
        subtitle = random.choice(choices)
        self.distribution[subtitle] += 1
        return subtitle
            
subtitle_distribution = SubtitleDistribution(lfj_subtitles)
@app.route("/")
@app.route('/home')
def main():
    navbar_collection.set_active("home")
    return render_template("main.html", subtitle=subtitle_distribution.get_subtitle(), \
        navbarItems=navbar_collection.get_tabs(), \
        skills=[('Programming', languages), ('Frameworks', frameworks), ('Tools', tools)])

@app.route('/projects')
def projects():
    navbar_collection.set_active("projects")
    return render_template('projects.html', navbarItems=navbar_collection.get_tabs())

@app.route('/contact')
def contacts():
    navbar_collection.set_active('contact')
    return render_template('contacts.html', navbarItems=navbar_collection.get_tabs())

@app.route('/work')
def work():
    navbar_collection.set_active('work')
    return render_template('work.html', navbarItems=navbar_collection.get_tabs())

@app.route("/<path:path>")
def badroute(path):
    return "Unfounded route: " + path

if __name__ == '__main__':
    if DEBUG:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0')
