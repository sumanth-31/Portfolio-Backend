"""portfolioBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from rest.views import (
    add_user,
    login,
    AddPost,
    is_authenticated,
    get_posts,
    DeletePost,
    DeleteCollection,
    UploadCollectionImage,
    DeleteTag,
    get_collections,
    get_tags,
    ChangePassword,
    UploadProfilePic,
    UploadResume,
    UploadTagImage,
    get_user,
    AddProject,
)

urlpatterns = [
    path("add_user/", add_user),
    path("admin/", admin.site.urls),
    path("login/", login),
    path("add_post/", AddPost.as_view()),
    path("is_auth/", is_authenticated),
    path("posts/", get_posts),
    path("delete_post/", DeletePost.as_view()),
    path("delete_collection/", DeleteCollection.as_view()),
    path("upload/collection_image/", UploadCollectionImage.as_view()),
    path("upload/tag_image/", UploadTagImage.as_view()),
    path("delete_tag/", DeleteTag.as_view()),
    path("collections/", get_collections),
    path("tags/", get_tags),
    path("change_password/", ChangePassword.as_view()),
    path("profile_pic/", UploadProfilePic.as_view()),
    path("upload/resume/", UploadResume.as_view()),
    path("user/", get_user),
    path("upload/project/", AddProject.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
