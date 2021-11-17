from django.shortcuts import render, redirect
from .models import *
from django.db.models import Max
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Behaves like @staticmethod
def text_to_html(oldText):
    oldText = oldText.replace("\r\n", "XiLBXZ")
    oldText = oldText.replace("\n", "XiLBXZ")
    oldText = oldText.replace("\r", "XiLBXZ")
    oldText = oldText.replace("\s", " ")
    oldText = oldText.strip()
    oldText = oldText.replace("XiLBXZXiLBXZ", "</p><p>")
    oldText = oldText.replace("XiLBXZ", "<br>")
    oldText = "<p>" + oldText + "</p>"
    oldText = oldText.replace("<p><\/p>", "")
    oldText = oldText.replace("\r\n\r\n", "")
    oldText = oldText.replace("<\/p><p>", "</p>\r\n\r\n<p>")
    oldText = oldText.replace("<p><br \/>", "<p>")
    oldText = oldText.replace("<p><br", "<p>")
    oldText = oldText.replace(" <\/p>", "</p>")
    return oldText


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user_is_authenticated = True
        allContents = Content.objects.filter(contentApproval="pending").order_by("-contentAddingTime")
    else:
        user_is_authenticated = False
        allContents = Content.objects.all().order_by("-contentAddingTime")
    allContentsList = []
    for item in allContents:
        if item.contentType == "kobita":
            allContentsList.append(item.kobita)
        elif item.contentType == "golpo":
            allContentsList.append(item.golpo)
        elif item.contentType == "chobi":
            allContentsList.append(item.chobi)
        elif item.contentType == "cinemareviews":
            allContentsList.append(item.cinemareviews)
        elif item.contentType == "boireviews":
            allContentsList.append(item.boireviews)
        elif item.contentType == "rannabanna":
            allContentsList.append(item.rannabanna)
        elif item.contentType == "probondho":
            allContentsList.append(item.probondho)
        elif item.contentType == "boi":
            allContentsList.append(item.boi)
        elif item.contentType == "other":
            allContentsList.append(item.other)

    if request.method == "POST":
        contentId = request.POST.get("contentId")
        acceptation = request.POST.get("accept")
        theContent = Content.objects.filter(contentId=contentId).first()
        if acceptation == "approve":
            theContent.contentApproval = "yes"
        elif acceptation == "decline":
            theContent.contentApproval = "no"
        else:
            theContent.contentApproval = "pending"
        theContent.save()
    
    context = {"allContents": allContents,"allContentsList": allContentsList, "user_is_authenticated" : user_is_authenticated }
    return render(request, "index.html", context)

def view_content(request, contentType):
    if contentType == "kobita":
        allView = Kobita.objects.all()
    elif contentType == "golpo":
        allView = Golpo.objects.all()
    elif contentType == "chobi":
        allView = Chobi.objects.all()
    elif contentType == "cinemareviews":
        allView = CinemaReview.objects.all()
    elif contentType == "boireviews":
        allView = BoiReview.objects.all()
    elif contentType == "rannabanna":
        allView = RannaBanna.objects.all()
    elif contentType == "probondho":
        allView = Probondho.objects.all()
    elif contentType == "boi":
        allView = BoiBahar.objects.all()
    elif contentType == "other":
        allView = Other.objects.all()
    
    context = {"contentType":contentType, "allView":allView}
    return render(request, "content.html", context)

def add_content(request):
    if request.method == "POST":
        contentType = request.POST.get("contentType")
        authorFirstName = request.POST.get("authorFirstName")
        authorLastName = request.POST.get("authorLastName")
        try:
            contentId = Content.objects.all().aggregate(Max('contentId'))['contentId__max'] + 1
        except:
            contentId = 1
        dateTime = datetime.now()
        if contentType == "kobita":
            kobitaText = request.POST.get("kobitaText")
            kobitaText = text_to_html(kobitaText)
            try:
                kobitaId = Kobita.objects.all().aggregate(Max('kobitaId'))['kobitaId__max'] + 1
            except:
                kobitaId = 1
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newKobita = Kobita(kobitaId = kobitaId, contentId = contentId_x, kobitaText=kobitaText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newKobita.save()
        
        elif contentType == "golpo":
            golpoText = request.POST.get("golpoText")
            golpoText = text_to_html(golpoText)
            try:
                golpoId = Golpo.objects.all().aggregate(Max('golpoId'))['golpoId__max'] + 1
            except:
                golpoId = 1
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newGolpo = Golpo(golpoId = golpoId, contentId = contentId_x, golpoText = golpoText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newGolpo.save()

        elif contentType == "chobi":
            chobiField = request.FILES['imageFile']
            chobiText = request.POST.get('golpoText')
            chobiText = text_to_html(chobiText)
            try:
                chobiId = Chobi.objects.all().aggregate(Max('chobiId'))['chobiId__max'] + 1
            except:
                chobiId = 1
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newchobi = Chobi(chobiId = chobiId, chobiField=chobiField, contentId = contentId_x, chobiText = chobiText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newchobi.save()

        elif contentType == "cinemaReview":
            try:
                cinemaReviewId = CinemaReview.objects.all().aggregate(Max('cinemaReviewId'))['cinemaReviewId__max'] + 1
            except:
                cinemaReviewId = 1
            cinemaReviewFile = request.FILES['videoField']
            cinemaReviewText = request.POST.get('golpoText')
            cinemaReviewText = text_to_html(cinemaReviewText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newCinemaReview = CinemaReview(cinemaReviewId = cinemaReviewId, cinemaReviewFile=cinemaReviewFile, contentId = contentId_x, cinemaReviewText = cinemaReviewText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newCinemaReview.save()
            
        elif contentType == "boiReview":
            try:
                boiReviewId = BoiReview.objects.all().aggregate(Max('boiReviewId'))['boiReviewId__max'] + 1
            except:
                boiReviewId = 1
            boiReviewFile = request.FILES['videoField']
            boiReviewText = request.POST.get('golpoText')
            boiReviewText = text_to_html(boiReviewText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newBoiReview = BoiReview(boiReviewId = boiReviewId, boiReviewFile=boiReviewFile, contentId = contentId_x, boiReviewText = boiReviewText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newBoiReview.save()

        elif contentType == "rannaBanna":
            try:
                rannaBannaId = RannaBanna.objects.all().aggregate(Max('rannaBannaId'))['rannaBannaId__max'] + 1
            except:
                rannaBannaId = 1
            rannaBannaFile = request.FILES['videoField']
            rannaBannaText = request.POST.get('golpoText')
            rannaBannaText = text_to_html(rannaBannaText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newRannaBanna = RannaBanna(rannaBannaId = rannaBannaId, rannaBannaFile=rannaBannaFile, contentId = contentId_x, rannaBannaText = rannaBannaText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newRannaBanna.save()
        
        elif contentType == "probondho":
            try:
                probondhoId = Probondho.objects.all().aggregate(Max('probondhoId'))['probondhoId__max'] + 1
            except:
                probondhoId = 1
            probondhoText = request.POST.get("golpoText")
            probondhoText = text_to_html(probondhoText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newProbondho = Probondho(probondhoId = probondhoId, contentId = contentId_x, probondhoText = probondhoText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newProbondho.save()

        elif contentType == "boiBahar":
            try:
                boiBaharId = BoiBahar.objects.all().aggregate(Max('boiBaharId'))['boiBaharId__max'] + 1
            except:
                boiBaharId = 1
            boiBaharFile = request.FILES['pdfField']
            boiBaharText = request.POST.get('golpoText')
            boiBaharText = text_to_html(boiBaharText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newBoiBahar = BoiBahar(boiBaharId = boiBaharId, boiBaharFile=boiBaharFile, contentId = contentId_x, boiBaharText = boiBaharText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newBoiBahar.save()

        elif contentType == "other":
            try:
                otherId = Other.objects.all().aggregate(Max('otherId'))['otherId__max'] + 1
            except:
                otherId = 1
            otherFile = request.FILES['videoField']
            otherText = request.POST.get('golpoText')
            otherText = text_to_html(otherText)
            newContent = Content(contentId = contentId, contentType = contentType, contentAddingTime = dateTime)
            newContent.save()
            contentId_x = Content.objects.get(contentId = contentId)
            newOtherObj = Other(otherId = otherId, otherFile=otherFile, contentId = contentId_x, otherText = otherText, authorFirstName=authorFirstName, authorLastName=authorLastName)
            newOtherObj.save()

        return redirect("/")
    return render(request, "addContent.html")

def logmein(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully :)")
            return redirect("/")
        else:
            messages.error(request, 'Incorrect username or password :(')
        #     return redirect("/login")
        # user = User.objects.create_user(username=username, password=password)
        # user.save()
        # messages.success(request, "Account created successfully")
        # return redirect("/logmein")
    
    return render(request, "logmein.html")