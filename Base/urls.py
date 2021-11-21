from os import name
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
app_name = "Base"

# Resigter the Model
router = routers.DefaultRouter()
# Here 'posts' is the name of the url which will be added after api/posts to get the data
router.register('posts',views.PostViewSet,basename='posts')
router.register('accounts',views.PostViewSet,basename='accounts')

urlpatterns = [
    # HomePage
    path('',views.HomeView,name="HomeView"),
    # View All Comments
    path('comments/<postslug>/',views.CommentView,name="CommentView"),
    # View All Likes
    path('Likes/<postslug>/',views.LikesView,name="LikesView"),
    # View Profile of a User
    path('Profile/<slug>/',views.ProfileView,name="ProfileView"),
    # Add a new Post
    path('Add-Post/',views.AddPost,name="AddPost"),
    # Explore Page
    path('Explore/',views.ExploreView,name="ExploreView"),
    # Show the individual Post
    path('Explore/<SearchInput>/',views.Search,name="ExploreSearch"),
    # Edit User profile
    path('Edit-Profile/<slug>/',views.ProfileEdit,name="ProfileEdit"),
    # All Chatrooms
    path('AllChats/',views.AllChats,name="AllChats"),
    # For entering chatroom of two people
    path('Chat/<user1>&&<user2>/',views.Chatroom,name="Chatroom"),
    # ajax to save messages
    path('Message/',views.SaveMessage,name="SaveMessage"),
    # ajax to save comment
    path('Comment/',views.SaveComment,name="SaveComment"),
    # ExplorePosts
    path('ExplorePosts/<slug>/',views.ExplorePosts,name="ExplorePosts"),
    # For Status Upload
    path('statusbar/',views.StatusView,name="StatusView"),
    # For Viewwing all the status
    path('Stories/<user>/',views.Statuses,name="StatusShow"),
    # ajax for follow and following
    path('FollowUnfollow/',views.AddRemFollower,name = "AddRemFollower"),
    # for sending Status Reply
    path('StatusReply/',views.SendReply,name = "SendReply"),

    # REST API
    # include the router urls
    path('api/', include(router.urls)),

    path('api/authentication/<username>/<password>/',views.AppLogin,name="AppLogin"),

]


if settings.DEBUG:

    urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



