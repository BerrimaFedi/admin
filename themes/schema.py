# themes/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import AdminTheme

class AdminThemeType(DjangoObjectType):
    class Meta:
        model = AdminTheme

class ApplyThemeMutation(graphene.Mutation):
    class Arguments:
        theme_id = graphene.ID(required=True)

    ok = graphene.Boolean()
    theme = graphene.Field(AdminThemeType)

    def mutate(self, info, theme_id):
        theme = AdminTheme.objects.get(pk=theme_id)
        AdminTheme.objects.update(is_active=False)
        theme.is_active = True
        theme.save()
        return ApplyThemeMutation(ok=True, theme=theme)

class Query(graphene.ObjectType):
    all_themes = graphene.List(AdminThemeType)

    def resolve_all_themes(self, info):
        return AdminTheme.objects.all()


class Mutation(graphene.ObjectType):
    apply_theme = ApplyThemeMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

