from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import views as blog_views
# (
#     index,
#     search,
#     post_list,
#     post_detail,
#     post_create,
#     post_update,
#     post_delete,
#     IndexView,
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     accept_offer,
#     AboutView
# )
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^accounts/', include('allauth.urls')),
    path('accounts/login/', include('allauth.urls')),
    path('accounts/logout/', include('allauth.urls')),
    # path('', index),
    path('', blog_views(), name='home'),
    path('home', blog_views.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', blog_views.as_view(), name='post-list'),
    path('search/', blog_views, name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    # path('create/', post_create, name='post-create'),
    path('create/', blog_views.as_view(), name='post-create'),
    # path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', blog_views.as_view(), name='post-detail'),
    # path('post/<id>/update/', post_update, name='post-update'),
    path('post/<pk>/update/', blog_views.as_view(), name='post-update'),
    # path('post/<id>/delete/', post_delete, name='post-delete'),
    path('post/<pk>/delete/', blog_views.as_view(), name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('accept_offer/<int:comment_id>/<int:asset_id>/'  , blog_views, name='accept-offer'),
    path('about/', blog_views , name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)