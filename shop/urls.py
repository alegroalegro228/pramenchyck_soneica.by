from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path("", views.products, name='main'),

    path("buy-now-page/<int:product_id>/", views.buy_now_page, name="buy_now_page"),
    path("buy-all-page/", views.buy_all_page, name="buy_all_page"),

    path("basket/add/<int:product_id>/", views.basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>/", views.basket_remove, name="basket_remove"),
    path("basket/product-plus/<int:basket_id>/", views.basket_product_plus, name="basket_product_plus"),
    path("basket/product-minus/<int:basket_id>/", views.basket_product_minus, name="basket_product_minus"),
    path("basket/", views.basket, name="basket"),

    path('<int:product_id>/', views.detail, name='detail'),

    path('catalog/guitars/', views.all_guitars_catalog, name='guitars'),
    path('catalog/keyboards/', views.all_keyboards_catalog, name='keyboards'),
    path('catalog/drums/', views.all_drums_catalog, name='drums'),
    path('catalog/studio-equipment/', views.all_studio_equipments_catalog, name='studio_equipment'),
    path('catalog/patch-cables/', views.all_patch_cables_catalog, name='patch_cables'),

    path('catalog/electric-guitars/', views.electric_guitars_catalog, name='electric_guitars_catalog'),
    path('catalog/bass-guitars/', views.bass_guitars_catalog, name='bass_guitars_catalog'),
    path('catalog/acoustic-guitars/', views.acoustic_guitars_catalog, name='acoustic_guitars_catalog'),
    path('catalog/classical-guitars/', views.classical_guitars_catalog, name='classical_guitars_catalog'),
    path('catalog/digital-pianos/', views.digital_pianos_catalog, name='digital_pianos_catalog'),
    path('catalog/synthesizers/', views.synthesizers_catalog, name='synthesizers_catalog'),
    path('catalog/midi-controllers/', views.midi_controllers_catalog, name='midi_controllers_catalog'),
    path('catalog/drum-kits/', views.drum_kits_catalog, name='drum_kits_catalog'),
    path('catalog/digital-drums/', views.digital_drums_catalog, name='digital_drums_catalog'),
    path('catalog/percussions/', views.percussions_catalog, name='percussions_catalog'),
    path('catalog/drum-accessories/', views.drum_accessories_catalog, name='drum_accessories_catalog'),
    path('catalog/audio-interfaces/', views.audio_interfaces_catalog, name='audio_interfaces_catalog'),
    path('catalog/studio-monitors/', views.studio_monitors_catalog, name='studio_monitors_catalog'),
    path('catalog/microphones/', views.microphones_catalog, name='microphones_catalog'),
    path('catalog/studio-headphones/', views.studio_headphones_catalog, name='studio_headphones_catalog'),
    path('catalog/dj-controllers/', views.dj_controllers_catalog, name='dj_controllers_catalog'),
    path('catalog/guitar-cables/', views.guitar_cables_catalog, name='guitar_cables_catalog'),
    path('catalog/microphone-cables/', views.microphone_cables_catalog, name='microphone_cables_catalog'),
    path('catalog/speaker-cables/', views.speaker_cables_catalog, name='speaker_cables_catalog'),
    path('catalog/midi-cables/', views.midi_cables_catalog, name='midi_cables_catalog'),

    path('detail/comment-delete/<int:comment_id>', views.comment_delete, name='comment_delete'),

    path('my-orders/', views.my_orders, name='my_orders')
]