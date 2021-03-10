from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


def group_required(groups=[]):
    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # raw_groups = request.user.groups.only('name')
            raw_groups = request.user.groups.all()
            user_group = set([group.name for group in raw_groups])

            if user_group.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed!')
        return wrapper
    return decorator


class GroupRequiredMixin:
    groups = None

    def dispatch(self, req, *args, **kwargs):
        user = req.user
        if not user.is_authenticated:
            raise PermissionDenied()

        groups_set = set(self.groups or [])
        raw_groups = user.groups.all()
        user_groups = set([group.name for group in raw_groups])

        if not user_groups.intersection(groups_set) and \
                not user.is_superuser:
            raise PermissionDenied()

        return super().dispatch(req, *args, **kwargs)
