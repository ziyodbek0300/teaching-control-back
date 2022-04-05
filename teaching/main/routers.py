from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register('users', UsersViewset)
router.register('jobs', JobsViewset)
router.register('sections', SectionViewset)
router.register('themes', ThemeViewset)