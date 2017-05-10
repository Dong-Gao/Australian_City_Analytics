from django.conf.urls import url,include
from cloud import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^index', views.HomePageView.as_view()),
    url(r'^scenario-one/$', views.scenario_oneView.as_view()),
    url(r'^scenario-two/$', views.scenario_twoView.as_view()),
    url(r'^scenario-three/$', views.scenario_threeView.as_view()),
    url(r'^scenario-two2/$', views.scenario_twoView2.as_view()),
    url(r'^scenario-three2/$', views.scenario_threeView2.as_view()),
    url(r'^team-member/$', views.team_memberView.as_view()),
]
