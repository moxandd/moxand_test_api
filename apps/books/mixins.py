from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class BookViewSetMixin(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass

class AuthorViewSetMixin(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass

class GenreViewSetMixin(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass