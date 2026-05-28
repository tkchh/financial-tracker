class UserOwnedQuerySetMixin:
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)