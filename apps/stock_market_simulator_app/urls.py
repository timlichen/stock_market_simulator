from django.conf.urls import url
from . import views

app_name = "stock_market_sim_app"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^symbol_lookup$', views.posted_historic_stock_data, name='post_symbol'),
]
