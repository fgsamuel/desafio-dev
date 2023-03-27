from django.contrib import admin

from cnab_reader.core.models import Store
from cnab_reader.core.models import Transaction

admin.site.site_header = "CNAB Reader"
admin.site.site_title = "CNAB Reader"
admin.site.index_title = "CNAB Reader Admin"

admin.site.register(Transaction)
admin.site.register(Store)
