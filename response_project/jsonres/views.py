from django.http import JsonResponse, HttpResponse
from django.template import loader


student_data = [
    {
        "id": 1,
        "name": "John Smith",
        "department": "Computer Science",
        "email": "john.smith@example.com",
    },
    {
        "id": 2,
        "name": "Mary Johnson",
        "department": "Electrical Engineering",
        "email": "mary.johnson@example.com",
    },
    {
        "id": 3,
        "name": "David Brown",
        "department": "Mechanical Engineering",
        "email": "david.brown@example.com",
    },
    {
        "id": 4,
        "name": "Emily Davis",
        "department": "Biology",
        "email": "emily.davis@example.com",
    },
    {
        "id": 5,
        "name": "Michael Lee",
        "department": "Physics",
        "email": "michael.lee@example.com",
    },
    {
        "id": 6,
        "name": "Sophia Wilson",
        "department": "Chemistry",
        "email": "sophia.wilson@example.com",
    },
    {
        "id": 7,
        "name": "Daniel Harris",
        "department": "History",
        "email": "daniel.harris@example.com",
    },
    {
        "id": 8,
        "name": "Olivia Turner",
        "department": "Psychology",
        "email": "olivia.turner@example.com",
    },
    {
        "id": 9,
        "name": "Matthew Martinez",
        "department": "Mathematics",
        "email": "matthew.martinez@example.com",
    },
    {
        "id": 10,
        "name": "Ava Jackson",
        "department": "English",
        "email": "ava.jackson@example.com",
    },
]


def jsonres(request):
    # Convert the list of dictionaries to JSON and return it as a response
    return JsonResponse(student_data, safe=False)


def htmlres(request):
    template = loader.get_template("htmlres.html")
    context = {
        "students": student_data,
    }
    return HttpResponse(template.render(context, request))


def mainres(request):
    template = loader.get_template("main.html")
    context = {
        "students": student_data,
    }
    return HttpResponse(template.render(context, request))


def textres(request):
    text_content = f"""This is a plain text response. Student Data is below.


{student_data}"""

    # Create a text response
    response = HttpResponse(text_content, content_type="text/plain")
    return response
