from django.contrib import admin
from django.utils import timezone

from multimedia.models import Multimedia, ArticleImage, Article, MultimediaVideo, MultimediaAudio


class MultimediaVideoAdmin(admin.StackedInline):
    model = MultimediaVideo
    fk_name = "multimedia"
    extra = 1
    min_num = 1
    max_num = 10
    can_delete = True
    verbose_name_plural = "Add Multimedia Video"


class MultimediaAudioAdmin(admin.StackedInline):
    model = MultimediaAudio
    fk_name = "multimedia"
    extra = 1
    min_num = 1
    max_num = 10
    can_delete = True
    verbose_name_plural = "Add Multimedia Audio"


def save_form_set(self, request, form, formset, change):
    if formset.model == Multimedia:
        instances = formset.save(commit=False)
        for instance in instances:
            instance.updated_by = request.user
            if instance.is_approved:
                instance.approved_by = request.user
                instance.approved_at = timezone.now()
            instance.save()
    else:
        formset.save()


@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    inlines = [MultimediaVideoAdmin, MultimediaAudioAdmin]

    list_display = ("title", "is_approved", "approved_at", "approved_by", "uploaded_by", "uploaded_at")

    fieldsets = (
        ("Media Information", {
            "classes": ("wide", "extrapretty"),
            "fields": ("title", "description")
        }),
        ("Business Information", {
            "classes": ("wide",),
            "fields": ("is_approved",)
        })
    )

    list_filter = ("is_approved",)
    search_fields = ("approved_by", "uploaded_by", "title", "description", "audio", "video")
    date_hierarchy = "uploaded_at"
    ordering = ("title", "is_approved", "approved_at", "approved_by", "uploaded_by", "uploaded_at")

    def save_model(self, request, obj, form, change):
        obj.uploaded_by = request.user
        if obj.is_approved:
            obj.approved_by = request.user
            obj.approved_at = timezone.now()
        obj.save()

    def save_formset(self, request, form, formset, change):
        save_form_set(self, request, form, formset, change)


class ArticleImageAdmin(admin.StackedInline):
    model = ArticleImage
    fk_name = "article"
    extra = 1
    min_num = 1
    max_num = 10
    can_delete = True
    verbose_name_plural = "Add Article Image"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin]

    list_display = ("title", "is_approved", "approved_at", "approved_by", "uploaded_by", "uploaded_at")
    list_filter = (
        ("is_approved", admin.BooleanFieldListFilter),
    )

    # update form for admin site
    fieldsets = (
        ("Article Information.", {
            "classes": ("wide", "extrapretty"),
            "fields": ("title", "description")
        }),

        ("Business Details", {
            "classes": ("wide", "extrapretty"),
            "fields": ("is_approved",)
        })
    )

    def save_model(self, request, obj, form, change):
        obj.uploaded_by = request.user
        if obj.is_approved:
            obj.approved_by = request.user
            obj.approved_at = timezone.now()
        obj.save()

    def save_formset(self, request, form, formset, change):
        save_form_set(self, request, form, formset, change)
