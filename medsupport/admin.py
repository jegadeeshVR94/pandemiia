from django.contrib import admin
from .models import Hospital,  Contact, \
    HospitalCategory, SolutionCategory, Need, Solution


class NeedInline(admin.TabularInline):
    model = Need
    fields = ('article', ('quantity_needed', 'quantity_done'), 'units', 'status')
    autocomplete_fields = ['article']
    extra = 1


class PointContactPersonInline(admin.TabularInline):
    model = Contact
    classes = ('collapse',)
    fields = ('point', 'full_name', 'position', 'phone', 'email')
    extra = 0


@admin.register(SolutionCategory)
class CategoryArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Solution)
class ArticleAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'category')
    search_fields = ('name',)
    filter_horizontal = ('category',)


@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    pass


@admin.register(HospitalCategory)
class CategoryPointAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Hospital)
class PointAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', ('name', 'description'))
        }),
        ('Категорія установи', {
            'classes': ('collapse',),
            'fields': ('category',)
        }),
        ('Адрес', {
            'classes': ('collapse',),
            'fields': (('region', 'city'), ('line1', 'zip_code'), ('geo_lat', 'geo_lng'))
        }),
        ('Додатково', {
            'classes': ('collapse',),
            'fields': (('company_code'), ('email'))
        }),
    )
    # readonly_fields = ('user',)
    filter_horizontal = ('category',)
    inlines = (PointContactPersonInline, NeedInline)

    def get_queryset(self, request):
        qs = super(PointAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

    def get_readonly_fields(self, request, obj=None):
        fields = list(super(PointAdmin, self).get_readonly_fields(request, obj))

        # add User field to read_only if user is not superuser
        if not request.user.is_superuser:
            fields.append('user')
        return fields
