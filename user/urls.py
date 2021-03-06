from django.contrib import admin
from django.urls import path,include
from user import views

app_name = "user"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/api/v1/signup/", views.SignUpView.as_view(), name="signup"),
    path("auth/api/v1/login/", views.LoginView.as_view(), name="login"),
    path("home/", views.Home.as_view()),

    # path("profile/api/v1/create/", views.CreateProfile.as_view(), name="profile"),
    path("profile/api/v1/list/", views.GetAllProfile.as_view(), name="profile_list"),
    path("profile/api/v1/get/<int:pk>/", views.GetProfile.as_view(), name="get_profile"),
    path("profile/api/v1/update/<int:pk>/", views.UpdateProfile.as_view(), name="update_profile"),
    path("profile/api/v1/delete/<int:pk>/", views.DeleteProfile.as_view(),name="delete_profile"),

    # Friend_Requests
    path("Friend_Request/api/v1/list/", views.GetAllFriendRequest.as_view(),),
    path("Friend_Request/api/v1/create/", views.CreateFriendRequest.as_view()),
    path("Friend_Request/api/v1/get/<int:pk>/", views.GetFriendRequest.as_view(),),
    path("Friend_Request/api/v1/update/<int:pk>/", views.UpdateFriendRequest.as_view(),),
    path("Friend_Request/api/v1/delete/<int:pk>/", views.DeleteFriendRequest.as_view()),

    # HostMatch
    path("host_match/api/v1/list/", views.GetAllHostMatch.as_view()),
    path("host_match/api/v1/create/", views.CreateHostMatch.as_view()),
    path("host_match/api/v1/get/<int:pk>/", views.GetHostMatch.as_view()),
    path("host_match/api/v1/update/<int:pk>/", views.UpdateHostMatch.as_view()),
    path("host_match/api/v1/delete/<int:pk>/", views.DeleteHostMatch.as_view()),
    # HostInvitation
    path("host_invitation/api/v1/list/", views.GetAllHostInvitation.as_view()),
    path("host_invitation/api/v1/create/", views.CreateHostInvitation.as_view()),
    path("host_invitation/api/v1/get/<int:pk>/", views.GetHostInvitation.as_view()),
    path("host_invitation/api/v1/update/<int:pk>/", views.UpdateHostInvitation.as_view()),
    path("host_invitation/api/v1/delete/<int:pk>/", views.DeleteHostInvitation.as_view()),


    # TeamScore
    path("team_score/api/v1/list/", views.GetAllTeamScore.as_view()),
    path("team_score/api/v1/create/", views.CreateTeamScore.as_view()),
    path("team_score/api/v1/get/<int:pk>/", views.GetTeamScore.as_view()),
    path("team_score/api/v1/update/<int:pk>/", views.UpdateTeamScore.as_view()),
    path("team_score/api/v1/delete/<int:pk>/", views.DeleteTeamScore.as_view()),
    
    path("notification/api/v1/update/<int:pk>/", views.CreateNotification.as_view()),
    path("notification1/api/v1/create/", views.NotificationsAPI.as_view()),
    
    #postman urls
    path('contact_us/',views.ContactUsAPI.as_view(),name="contactus"),
    path('list_contact_us/',views.getContactUsAPI.as_view(),name="contactus"),
    path('about_us/',views.AboutUsAPI.as_view(),name="aboutus"),
    path('privacy_policy/',views.PrivacyPolicyAPI.as_view(),name="privacypolicy"),
    path('terms_conditions/',views.TermsConditionAPI.as_view(),name="termsconditions"),
    path('reset_password/',views.ResetPasswordAppAPI.as_view(),name="resetpassword"),
    path(
        "auth/api/v1/forgot-password-email/",
        views.RequestPasswordResetEmailView.as_view(),
        name="forgot-password-email",
    ),
    path(
        "auth/api/v1/forgot-password/<uidb64>/<token>/",
        views.PasswordTokenCheckAPIView.as_view(),
        name="forgot-password-confirm",
    ),
    path(
        "auth/api/v1/forgot-password-complete/",
        views.SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    #postman API for friend request
    path('invitations/',views.Invitations.as_view()),
    path('accept_friend_request/',views.MyFriends_Accepted.as_view()),
    path('friend_request_send/',views.Friend_Request_Send.as_view()),
    path('accept_request/',views.Accept_Request.as_view()),
    path('decline_friend_request/',views.Decline_Friend_Request.as_view()),

    #postman API for hostinvitation
    path('hostmatch_invitation/',views.HostMatch_Invitations.as_view()),
    path('accept_hostMatch_request/',views.Accept_HostMatch_Request.as_view()),
    path('decline_hostmatch_request/',views.Decline_Hostmatch_Request.as_view()),
    path('accepted_hostmatches/',views.Myhostmatch_Accepted.as_view()),
]