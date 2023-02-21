from django.shortcuts import render
from .models.Combatants import Combatants
from .models.Pictures import Pictures
from .models.BGPictures import BGPictures
from .models.Videos import Videos
from .models.Places import Places
from userprofile.models import UserProfile


def response_about(request):
    context = {
        "bg_image": BGPictures.get_main_picture(),
        "admin_info": UserProfile.get_admin_info()
    }
    return render(request, "about.html", context=context)


def response_about_project(request):
    return render(
        request, "about_project.html",
        context={"bg_image": BGPictures.get_main_picture(), "admin_info": UserProfile.get_admin_info()}
    )


def response_find_form(request):
    places = Places.get_all_places()
    ranks = Combatants.get_all_ranks()

    context = {
        "places": places,
        "ranks": ranks,
        "bg_image": BGPictures.get_main_picture(),
        "admin_info": UserProfile.get_admin_info()
    }

    return render(request, "find_form.html", context)


def response_found_documents(request):
    query = Combatants.objects
    if request.POST["name"]:
        query = query.filter(name=request.POST["name"])
    if request.POST["surname"]:
        query = query.filter(name=request.POST["surname"])
    if request.POST["patronymic"]:
        query = query.filter(patronymic=request.POST["patronymic"])
    if request.POST["rank"] and request.POST["rank"] != "None":
        query = query.filter(rank=request.POST["rank"])
    if request.POST["battalion"]:
        query = query.filter(battalion=request.POST["battalion"])
    if request.POST["issue_year"]:
        query = query.filter(issue_year=request.POST["issue_year"])
    if request.POST["date_of_birth"]:
        query = query.filter(date_of_birth=request.POST["date_of_birth"])
    if request.POST["date_of_death"]:
        query = query.filter(date_of_death=request.POST["date_of_death"])
    if request.POST["place_of_birth"] and request.POST["place_of_birth"] != "None":
        place_of_birth = Places.objects.filter(place=request.POST["place_of_birth"]).first()
        if place_of_birth:
            query = query.filter(place_of_birth=place_of_birth)

    documents = query.all()
    if len(documents) == 0:
        documents = None
    context = {
        "documents": documents,
        "bg_image": BGPictures.get_main_picture(),
        "admin_info": UserProfile.get_admin_info()
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
        "video": video,
        "bg_image": BGPictures.get_main_picture(),
        "admin_info": UserProfile.get_admin_info()
    }

    return render(request, "document.html", context)
