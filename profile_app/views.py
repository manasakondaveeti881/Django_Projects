'''from django.shortcuts import render
from django.http import HttpResponse


# Profile Page View
def profile_page(request):

    # Dictionary data sent to HTML page
    data = {

        "name": "Manasa",
        "email": "manasa@gmail.com",
        "phone": "9876543210",
        "location": "Andhra Pradesh",

        "profession": "Python Full Stack Developer",
        "experience": "Fresher",
        "education": "B.Tech",

        "skills": [
            "Python",
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
            "MySQL"
        ],

        "projects": [
            "Employee Management System",
            "Portfolio Website",
            "Student Database Project"
        ]
    }

    return render(request, "profile.html", data)


# Contact Page View
def contact_page(request):

    message = ""

    # Check form submission
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        # Print data in terminal
        print(name)
        print(email)
        print(message_text)

        message = "Form Submitted Successfully!"

    return render(request, "contact.html", {"message": message})
from django.shortcuts import render

def grade_view(request, marks):
    marks = int(marks)

    if marks > 80:
        result = "Grade A"
    elif marks > 60:
        result = "Grade B"
    else:
        result = "FAIL"

    context = {
        "marks": marks,
        "result": result
    }

    return render(request, "grade.html", context)
from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Manasa", "email": "manasa@gmail.com"},
        {"name": "Appu", "email": "appu@gmail.com"},
        {"name": "Pavani", "email": "pavani@gmail.com"},
    ]

    return render(request, "students.html", {"students": students}'''
from django.shortcuts import render

# temporary storage (list)
students = []

def student_form(request):
    global students

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        students.append({
            "name": name,
            "email": email
        })

    return render(request, "students_form.html", {"students": students})