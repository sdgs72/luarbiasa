from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import luarbiasa.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', luarbiasa.views.index, name='index'),
    url(r'^index/$', luarbiasa.views.index, name='index'),
    url(r'^home/$', luarbiasa.views.index, name='index'),
    url(r'^search-result/$', luarbiasa.views.search_result, name='search-result'),
    url(r'^user-admin/$', luarbiasa.views.user_admin, name='user-admin'),
    url(r'^myadmin/$', luarbiasa.views.myAdmin, name='myadmin'),

    url(r'^register/$',luarbiasa.views.register,name='register'),
    url(r'^login/$',luarbiasa.views.login_view,name='login'),
    url(r'^logout/$',luarbiasa.views.logout_view,name='logout'),

    #### AJAX - URLS ###
    url(r'^getBannersByLocation/$', luarbiasa.views.getBannersByLocation, name='getBannersByLocation'),
    url(r'^getBannersByLocationCreditCard/$', luarbiasa.views.getBannersByLocationCreditCard, name='getBannersByLocationCreditCard'),
	### default django urls ###    
    url(r'^admin/', include(admin.site.urls)),

]

