from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Base"

urlpatterns = [

    path('',views.HomeView,name="HomeView"),
    path('comments/<postslug>/',views.CommentView,name="CommentView"),
    path('Likes/<postslug>/',views.LikesView,name="LikesView"),
    path('Profile/<slug>/',views.ProfileView,name="ProfileView"),
    path('Add-Post/',views.AddPost,name="AddPost"),
    path('Explore/',views.ExploreView,name="ExploreView"),
    path('Explore/<SearchInput>/',views.Search,name="ExploreSearch"),
    path('Edit-Profile/<slug>/',views.ProfileEdit,name="ProfileEdit"),
    path('AllChats/',views.AllChats,name="AllChats"),
    path('Chat/<user1>&&<user2>/',views.Chatroom,name="Chatroom"),
    # ajax to save messages
    path('Message/',views.SaveMessage,name="SaveMessage"),
    # ajax to save comment
    path('Comment/',views.SaveComment,name="SaveComment"),
    #ExplorePosts
    path('ExplorePosts/<slug>/',views.ExplorePosts,name="ExplorePosts"),
    #For Status Upload
    path('statusbar/',views.StatusView,name="StatusView"),
    # For Viewwing all the status
    path('Stories/',views.Statuses,name="StatusShow"),
    # ajax for follow and following
    path('FollowUnfollow/',views.AddRemFollower,name = "AddRemFollower")

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



