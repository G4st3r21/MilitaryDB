from django.shortcuts import render
from .models.Combatants import Combatants
from .models.Pictures import Pictures
from .models.Videos import Videos
from .models.Places import Places


def request_find_form(request):
    places = Places.objects.all()

    return render(request, "find_form.html", context={"places": places})


def response_found_documents(request):
    name = request.POST["name"]
    surname = request.POST["surname"]

    query = Combatants.objects.filter(name=name, surname=surname)
    if request.POST["patronymic"]:
        query = query.filter(patronymic=request.POST["patronymic"])
    if request.POST["rank"]:
        query = query.filter(rank=request.POST["rank"])
    if request.POST["battalion"]:
        query = query.filter(battalion=request.POST["battalion"])
    if request.POST["issue_year"]:
        query = query.filter(issue_year=request.POST["issue_year"])
    if request.POST["date_of_birth"]:
        query = query.filter(date_of_birth=request.POST["date_of_birth"])
    if request.POST["date_of_death"]:
        query = query.filter(date_of_death=request.POST["date_of_death"])
    if request.POST["place_of_birth"]:
        place_of_birth = Places.objects.filter(place=request.POST["place_of_birth"]).first()
        if place_of_birth:
            query = query.filter(place_of_birth=place_of_birth)

    documents = query.all()
    context = {
        "documents": documents
    }

    return render(request, "found_documents.html", context=context)


def response_document(request, document_id: int):
    combatant = Combatants.objects.filter(id=document_id).first()
    main_picture = Pictures.objects.filter(combatant=combatant, is_main_picture=True).first()
    other_pictures = Pictures.objects.filter(combatant=combatant, is_main_picture=False).all()
    video = Videos.objects.filter(combatant=combatant).first()

    context = {
        "combatant": combatant,
        "main_picture": main_picture,
        "other_pictures": other_pictures,
        "video": video
    }

    return render(request, "document.html", context)
