from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # add this back in later
    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=CASCADE)
    created_by = models.ForeignKey(User, related_name='', on_delete=CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits='5', decimal_places='2')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name

# --------------------------------------------- #

# dont think I'll need this for dagger's products
# CATEGORY_CHOICES = (
#     ('M', 'Merch'),
#     ('B', 'Beans'),
# )

# SIZE_CHOICES = (
#     ('S', '12oz'),
#     ('M', '2lb'),
#     ('L', '5lb'),
# )

# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     size = models.CharField(choices=SIZE_CHOICES, max_length=3, default='S')
#     slug = models.SlugField()
#     description = models.TextField()
#     image = models.ImageField()

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("core:product", kwargs={
#             'slug': self.slug
#         })

#     def get_add_to_cart_url(self):
#         return reverse("core:add-to-cart", kwargs={
#             'slug': self.slug
#         })

#     def get_remove_from_cart_url(self):
#         return reverse("core:remove-from-cart", kwargs={
#             'slug': self.slug
#         })

#     class Meta:
#         verbose_name_plural = "Items"

# class OrderItem(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return self.title

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"

#     def get_total_item_price(self):
#         return self.quantity * self.item.price

#     def get_total_discount_item_price(self):
#         return self.quantity * self.item.discount_price

#     def get_amount_saved(self):
#         return self.get_total_item_price() - self.get_total_discount_item_price()

#     def get_final_price(self):
#         if self.item.discount_price:
#             return self.get_total_discount_item_price()
#         return self.get_total_item_price()

# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     # ref_code = models.CharField(max_length=20, blank=True, null=True)
#     # shipping_address = models.ForeignKey(
#     #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     # billing_address = models.ForeignKey(
#     #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
#     # payment = models.ForeignKey(
#     #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     # coupon = models.ForeignKey(
#     #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
#     # being_delivered = models.BooleanField(default=False)
#     # received = models.BooleanField(default=False)
#     # refund_requested = models.BooleanField(default=False)
#     # refund_granted = models.BooleanField(default=False)

#     '''
#     1. Item added to cart
#     2. Adding a billing address
#     (Failed checkout)
#     3. Payment
#     (Preprocessing, processing, packaging etc.)
#     4. Being delivered
#     5. Received
#     6. Refunds
#     '''

#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         if self.coupon:
#             total -= self.coupon.amount
#         return total

#     def __str__(self):
#         return self.user.username
