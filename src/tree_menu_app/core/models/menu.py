from django.db import models


class Menu(models.Model):
    """Describes the fields and attributes of the Menu model in the database."""

    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        """Describes class metadata."""

        db_table = "menu"


class MenuItem(models.Model):
    """Describes the fields and attributes of the Menu Item model in the database."""

    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=150, blank=True)
    menu = models.ForeignKey(to="Menu", on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True, related_name="child")
    url = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def create_url(self) -> str:
        if self.parent:
            url = f"{self.parent.url}{self.name}"
        else:
            url = f"/{self.menu.name}/{self.name}/"
        if url[-1] != "/":
            url += "/"
        return url

    class Meta:
        """Describes class metadata."""

        db_table = "menu_items"
