from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="описание",
        help_text="Введите краткое описание категории",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/category_images",
        verbose_name="изображение",
        help_text="Загрузите изображение продукта",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="Введите наименование продукта",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(
        verbose_name="описание",
        help_text="Введите краткое описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/product_images",
        verbose_name="изображение",
        help_text="Загрузите изображение продукта",
    )
    price = models.IntegerField(
        verbose_name="цена за покупку",
        help_text="Введите цену за покупку",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        max_length=20,
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="Введите дату создания заказа",
    )
    updated_at = models.DateField(
        max_length=20,
        verbose_name="дата последнего изменения",
        help_text="Введите дату последнего изменения заказа",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Подукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "description",
            "category",
            "price",
            "created_at",
            "updated_at",
        ]

    def __str__(self):
        return self.name
