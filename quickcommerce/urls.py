from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ( LandingPageView,BrandStoresView,CategoryStoresView,StoreDetailView,AddToCartView,ProductDetailView, CartPageView,OrderDetailView, CheckoutPageView, MyAccountPageView,WishlistToggleView,SignupView,LoginView,VerifyEmailView, AdminDashboardView, ManagerDashboardView, StaffDashboardView,BannerView,
CustomerListView,ProductListView,CouponListView, CouponDetailView,ApplyCouponView,VendorDetailView, VendorListView,
CategoryDetailView, CategoryListView,BrandListView, BrandDetailView,OrderUpdateView, OrderCreateView, OrderListView,
ReturnRequestUpdateView, ReturnRequestListView,MediaPageView,LogoutView,PasswordResetView, DashboardStatisticsView,VendorInventoryView, ShippingIntegrationView )
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import dash_customer
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #frontend urls for user
    path('api/landing/', LandingPageView.as_view(), name='landing-page'),
    path('api/cart/', CartPageView.as_view(), name='cart-page'),
    path('api/cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/checkout/', CheckoutPageView.as_view(), name='checkout-page'),
    path('order/<uuid:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),

    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('api/wishlist/', WishlistToggleView.as_view(), name='wishlist-page'),
    path('api/my-account/', MyAccountPageView.as_view(), name='my-account-page'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api/stores-by-category/', CategoryStoresView.as_view(), name='stores-by-category'),
    path('api/stores-by-brand/', BrandStoresView.as_view(), name='stores-by-brand'),
    path('store/<slug:store_slug>/', StoreDetailView.as_view(), name='store-detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),

    #backend urls for dashboard

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('api/manager-dashboard/', ManagerDashboardView.as_view(), name='manager_dashboard'),
    path('api/staff-dashboard/', StaffDashboardView.as_view(), name='staff_dashboard'),
    path('api/media/', MediaPageView.as_view(), name='media_list'),
    path('api/banners/', BannerView.as_view(), name='banner_list'),
    path('api/banners/<uuid:pk>/', BannerView.as_view(), name='banner_detail'),
    path('cart/apply-coupon/', ApplyCouponView.as_view(), name='apply-coupon'),

    path('api/users/customers/', CustomerListView.as_view(), name='customer_list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<uuid:pk>/', ProductListView.as_view(), name='product-detail'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
    path('coupons/<uuid:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
    path('api/vendor/', VendorListView.as_view(), name='vendor-list'),
    path('api/vendor/<uuid:id>/', VendorDetailView.as_view(), name='vendor-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<uuid:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/<uuid:id>/', BrandDetailView.as_view(), name='brand-detail'),

    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<uuid:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('return-requests/', ReturnRequestListView.as_view(), name='return-request-list'),
    path('return-requests/<int:pk>/update/', ReturnRequestUpdateView.as_view(), name='return-request'),
    path('dashboard/statistics/', DashboardStatisticsView.as_view(), name='dashboard-statistics'),
    path('vendor/inventory/', VendorInventoryView.as_view(), name='vendor-inventory'),
    path('vendor/orders/<uuid:order_id>/ship/', ShippingIntegrationView.as_view(), name='ship-order'),
    path('vendor/orders/<uuid:order_id>/status/', ShippingIntegrationView.as_view(), name='fetch-delivery-status'),
    path('dashboard/customers', dash_customer, name='dash_customer'),
    # path('wishlist/', WishlistToggleView.as_view(), name='wishlist-toggle'),





    # Add other URL patterns here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# use for passing location coordinates rest normal0
# GET /api/landing/?latitude=37.7749&longitude=-122.4194

#to create auth tokens and include this token in headers from react while making a get request to any api
# python manage.py drf_create_token <username>


#pass category id or brand id for filtering their views (also location coordinates or saved_address_id)

