from django.urls import path
from rsk  import views
app_name="rsk" #is used to create a namespace(called url mapping)

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact")
    #path("secondary suffix",address of function,name of mapping)
]
