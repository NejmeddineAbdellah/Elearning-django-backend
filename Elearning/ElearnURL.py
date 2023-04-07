from django.urls import path
from .views import etudiant_list, enseignant_list, cours_list, inscription_list, addnew
from Elearning import views


urlpatterns = [
    #path('products/', product_list, name='product_list'),
    path('etudiants/', etudiant_list, name='etudiant_list'),
    path('enseignants/', enseignant_list, name='enseignant_list'),
    path('cours/', cours_list, name='cour_list'),
    path('', inscription_list, name='inscri_list'),
    path('addEtudiant/', addnew, name='addnewEtudiant'),
    path("EditEtudiant/<int:id>", views.edit, name="edit"),
    path("update/<int:id>", views.update, name="update"),
    path("addnew", views.addnew, name="addnew"),
    path("delete/<int:id>", views.delete, name="delete")

]