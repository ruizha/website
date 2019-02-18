from flask import Flask, render_template
import random
import enum

app = Flask(__name__)
DEBUG = False

class NavbarItem:
    def __init__(self, id_, name, href, active=False):
        self.name = name
        self.id = id_
        self.href = href
        self.active = active

class Skill:
    def __init__(self, title, proficiency):
        self.title = title
        self.proficiency, self.color = proficiency


class SkillList:
    def __init__(self, header, skills_list):
        self.header = header
        self.skills_list = skills_list

class Academic:
    def __init__(self, title, code, text):
        self.title = title
        self.code = code
        self.text = text

class Work:
    def __init__(self, title, company, location, description):
        self.title = title
        self.company = company
        self.location = location
        self.description = description

class Project:
    def __init__(self, title, duration, text):
        self.title = title
        self.duration = duration
        self.text = text

class PROFICIENCY:
    NOKNOWLEDGE = ("clueless", '#aaaaaa')
    THEORETICAL = ("heard of it", '#f9db89')
    PRACTICAL = ("kinda know", '#96eaa7')
    COMFORTABLE = ("comfortable", "#84e0d1")
    ADEPT = ("adept", "#a5c7ff")

navitems = [
    NavbarItem("home", "Home", "/home"),
    NavbarItem("work", "Where I Worked", "/work"),
    NavbarItem("projects", "Projects", "/projects"),
    NavbarItem("contact", "More About Me", "/contacts")
]

langs = SkillList("Programming Languages", [
    Skill("Python", PROFICIENCY.ADEPT),
    Skill("Javascript", PROFICIENCY.ADEPT),
    Skill("Java", PROFICIENCY.ADEPT),
    Skill("Kotlin", PROFICIENCY.COMFORTABLE),
    Skill("C/C++", PROFICIENCY.COMFORTABLE),
    Skill("SQL", PROFICIENCY.COMFORTABLE),
    Skill("HTML", PROFICIENCY.ADEPT),
    Skill("CSS", PROFICIENCY.COMFORTABLE)
])

frameworks = SkillList("Frameworks", [
    Skill("Flask", PROFICIENCY.ADEPT),
    Skill("Django", PROFICIENCY.ADEPT),
    Skill("RxJava", PROFICIENCY.COMFORTABLE),
    Skill("Android", PROFICIENCY.COMFORTABLE),
    Skill("Node.js", PROFICIENCY.ADEPT),
    Skill("Express.js", PROFICIENCY.COMFORTABLE),
    Skill("Nginx", PROFICIENCY.PRACTICAL),
    Skill("Docker", PROFICIENCY.PRACTICAL)
])

tools = SkillList("Tools", [
    Skill("Linux", PROFICIENCY.COMFORTABLE),
    Skill("Git", PROFICIENCY.COMFORTABLE),
    Skill("vim", PROFICIENCY.COMFORTABLE),
    Skill("AWS", PROFICIENCY.COMFORTABLE)
])

classes = [
    Academic("Distributed Systems", "01:198:417", "Allowed me to better understand how machines and clusters communicate, scale, and deal with failures"),
    Academic("Design and Analysis of Algorithms", "01:198:344", "Gave me an in-depth look and a greater understanding of the strengths and weaknesses of algorithms and how to apply them in different situation"),
    Academic("Principles of Information and Database Management", "01:198:366", "Gave me a lot of insight into the interworkings of the backbone of every system"),
    Academic("Intro. to Artificial Intelligence", "01:198:440", "I took this class expecting to because I wanted to work with artificial intelligence. I came out of it wanting to work with Big Data because I learned that is what I really wanted to do."),
    Academic("Operating Systems", "01:198:416", "While I do not really see myself doing any OS programming in the near future, this class is extremely useful to me whenever I am doing low-level programming such as using C/C++ and working with microprocessors. The information about memory management is also very helpful in understanding garbage collectors of various languages, interpreters, and compilers (especially those times when the JVM starts leaking memory)."),
    Academic("Computer Architectures", "01:198:211", "I learned how C works and found myself oddly enjoying it. Assembly and the execution stack were also pretty cool."),
]

links = {
    "home": "/",
    "projects": "/projects",
    "work": "/work",
    "contacts": "/contacts"
}

works = [
    Work("Engineering Intern", "Big Huge Games", "Jan. 2019 - Apr. 2019", "I was always very curious about video games and how it is all made. Therefore, after receiving my bachelors in Computer Science from Rutgers University and before I start my full-time role, I took an internship with BHG, embedded as an engineering intern in Core Tech and Tools. I work with a variety of technologies including Spring Boot, Python 3, .NET, amongst others improve libraries and applications already in use throughout the organization. Working there has opened my eyes about the requirements of systems that are both low latency and highly available."),
    Work("Summer Technical Analyst", "Royal Bank of Canada (RBC) Capital Markets", "Jun. 2018 - Aug. 2018", "During the summer 2018, I worked as a Technical Summer Analyst at Royal Bank of Canada Capital Markets. Working with a brilliant team of 17 interns and engineers, we developed an API Portal so that engineers have a central place to catalogue the libraries available as well as their documentation. We used Django, Python 3, and SQL Server to build the backend and for data storage. React.js and SASS were used to build the frontend. During the internship, I learned how to work in a large organization and Agile, working to meet the demands of the stakeholders."),
    Work("Student Developer", "Rutgers University EAS - Open Systems Solutions", "Jan. 2017 - Dec. 2018", "Starting in sophomore year, I worked as a Student Developer for OIT-Open Systems Solutions, a student-led department that developed the official Rutgers Application as well as several other services. I started as an Android developer and later on transitioned to working on the Express.js backend for the mobile application. We used a variety of tools, such as Express.js, Flask, MongoDB, and MariaDB."),
]

project_list = [
    Project("Royal Bank of Canada API Catalogue", "Jun. 2018 - Aug. 2018", "RBCCM has a large number of internal APIs developed by its many teams, from traders to programmers, and there should be a central place where people can search and experiment with the APIs. As such, the 2018 Summer Intern Class was tasked with creating an API Catalogue where RBC developers can onboard their APIs and have it be visible to RBCCM as well as other groups such as Investor and Treasury Services. Every team performed in a full-stack capacity, designing and implementing both frontend and backend. The application was built by following MVC principles. We made a RESTful backend using Django REST Framework and SQL Server. We developed a responsive frontend using React.js and SASS. We deployed to a Redhat Linux Machine using JenkinsCI. Application was tested using Python's unittest and Nose libraries."),
    Project("Rutgers Android Application", "Jan. 2017 - Dec. 2018", "During the semester, I work on the official Rutgers Android Application at Rutgers OIT-OSS which is used by 30,000+ simultaneous users. The application is built using MVP principles. RxJava is used extensively throughout the application in conjunction with Retrofit2 for Async I/O and state/event management. FCM/GCM is used to send notifications to users regarding bus arrivals and departures (and whatever other notices that we are required to send). Other libraries that we use include Picasso for image processing and Apache Commons. Application was tested using JUnit."),
    Project("Rutgers Mobile Backend", "Mar. 2017 - Dec. 2018", "In addition to the mobile application, I also develop the backend that serves as a data aggregation service, pulling data from various departments and services, like Transloc for monitoring the University's bus system and Schedule of Classes for class availability and scheduling, converting them into a standardized format, before delivering it to Android and iOS clients. It is a RESTful API built using Express.js. MongoDB is used for data storage. It is containerized on Docker and Docker Swarm so the application can be deployed on E-Discovery VMs. Mocha and Chai are used for unit tests."),
    Project("HackRU Ideaboard", "Sep. 2017 - Nov. 2017", "The primary goal of a hackathon is working on a team to solve a particular problem. But unless one comes with a team in mind, finding that team might be difficult. I helped to build the Ideaboard for HackRU, which is meant to help HackRU attendees form groups. Ideaboard is a Slackbot that allows attendees to list their project ideas and see the ideas of others, so that everyone could see if there is any project that interests them. So instead of having to ask around and potentially miss the chance to help on a project that one likes, one can just use the Ideaboard, see all the projects that are recruiting and what skills the project requires, and sign on with them."),
    Project("InvestWell", "Oct. 2018", "Project for HackRU Fall 2018 where we developed an application to give financial advice to users based on users with similar financial backgrounds. We used the Yodlee API to gather data about users, extracting only non-identifying information about each user, and cluster using K-Means. We used a Multi-Layer Perceptron to determine the fitness of a person's portfolio based on others in the cluster. Frontend was built using Angular.js, backend in Flask and MongoDB. For machine learning we used scikit-learn. Oh, it won 3rd place overall so yay!")
]

lfj_subtitles = [
    'Looking for job',
    '"...a fine choice" ~ everyone',
    '<span><a class=\'text-link\' href="https://www.dropbox.com/s/nvtbp6si16ng24b/rui_zhang_resume.pdf?dl=1" style="text-decoration: none;">Here\'s my resume</a></span>',
    'Graduating this semester',
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
    'Spittin\' Hot Lines',
    'Vim and Emacs are both good',
    'Preventing Segfaults',
    'Driven by a Natural Neurel Net',
    'I sometimes use a light theme',
    '<br>Traceback (most recent call last):<br><span style="padding-left: 2em">File "&lt;main.py&gt;", line 1, in</span> -- <br>jk I unittested this'
]

class SubtitleDistribution:
    def __init__(self, subtitles):
        pass

    def get_subtitle(self):
        return random.choice(subtitles)
            
subtitle_distribution = SubtitleDistribution(subtitles)


def set_active_navitem(tab):
    for nav in navitems:
        if nav.id != tab and nav.active:
            nav.active = False
        if nav.id == tab:
            nav.active = True

@app.route("/")
@app.route('/home')
def main():
    set_active_navitem('home')
    return render_template('home.html', subtitle="Full-Stack Developer", navitems=navitems, links=links,
                            skills_groups=[langs, frameworks, tools], classes=classes)

@app.route('/work')
def work():
    set_active_navitem('work')
    return render_template('work.html', works=works, navitems=navitems)

@app.route('/projects')
def projects():
    set_active_navitem('projects')
    return render_template('projects.html', projects=project_list, navitems=navitems)

@app.route('/contacts')
def contacts():
    set_active_navitem('contacts')
    return render_template('contacts.html', navitems=navitems)

if __name__ == '__main__':
    if DEBUG:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0')
