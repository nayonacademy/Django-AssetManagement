from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^members/$', views.members, name='members'),
	url(r'^members/(?P<id>[0-9]+)$', views.membersdetails, name='members'),
	url(r'^members/membersupdate/([0-9]+)$', views.membersupdate, name='membersupdate'),
	url(r'^members/membersdelete/([0-9]+)$', views.membersdelete, name='membersdelete'),
	url(r'^addmembers/$', views.addmembers, name='addmembers'),
	url(r'^assets/$', views.assets, name='assets'),
	url(r'^assets/(?P<id>[0-9]+)$', views.assetsdetails, name='assets'),
	url(r'^assets/assetupdate/([0-9]+)$', views.assetupdate,name='assetupdate'),
	url(r'^assets/assetdelete/([0-9]+)$', views.assetdelete,name='assetdelete'),
	url(r'^addasset/$', views.addasset, name='addasset'),
	url(r'^distribution/$', views.distribution, name='distribution'),
	url(r'^show_distribution/distributionupdate/(?P<id>[0-9]+)$', views.distributionupdate, name='distributionupdate'),
	url(r'^show_distribution/distributiondelete/(?P<id>[0-9]+)$', views.distributiondelete, name='distributiondelete'),
	url(r'^show_distribution/$', views.index, name='show_distribution'),
]