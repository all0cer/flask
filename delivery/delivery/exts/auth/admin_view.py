from flask_admin.contrib.sqla import ModelView

def format_user(obj, request, user, *args):
    return user.email.split("@")[0]

class UserAdmin(ModelView):
    """Admin interface"""

    column_formatters = {"email" : format_user}
    column_list = {"email", "admin"}
    column_searchable_list = ["email"]
    column_filters = ["email", "admin"]

    can_create = False
    can_delete = False
    can_edit = False

