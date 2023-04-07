from django.shortcuts import render, redirect
from .models import Etudiant, Enseignant, Cours, Inscription, Patient
from .forms import EtudiantForm
from faker import Faker


"""================Etudiants=============="""
def etudiant_list(request):
    f = Faker()
    etudiants = Etudiant.objects.all()
    for i in range(2):
        nom = f.name()
        prenom = f.name()
        email= f.email()
        etudiant=Etudiant(None,nom,prenom,email)
        etudiant.save()
    return render(request, 'etudiant_list.html', {'etudiants': etudiants})


def addnew(request):
    if request.method == "POST":  
        form = EtudiantForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/etudiants')
            except:  
                pass
    else:  
        form = EtudiantForm()
    return render(request,'AddEtudiant.html',{'form':form})


def edit(request, id):
    etudiant = Etudiant.objects.get(id=id)
    return render(request,'EditEtudiant.html', {'etudiant':etudiant})

def update(request, id):
    etudiant = Etudiant.objects.get(id=id)
    form = EtudiantForm(request.POST, instance = etudiant)
    if form.is_valid():
        form.save()
        return redirect("/etudiants")
    return render(request, 'EditEtudiant.html', {'etudiant': etudiant})

def delete(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return redirect("/etudiants")

"""==========================================="""



"""================Enseignants=============="""
def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignant_list.html', {'enseignants': enseignants})
"""==========================================="""



"""================Cours=============="""
def cours_list(request):
    cours = Cours.objects.all()
    return render(request, 'cours_list.html', {'cours': cours})
"""==========================================="""



"""================Inscription=============="""
def inscription_list(request):
    inscriptions = Inscription.objects.all()
    return render(request, 'inscription_list.html', {'inscriptions': inscriptions})


"""==========================================="""
