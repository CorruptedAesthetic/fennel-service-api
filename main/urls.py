from django.urls import include, path
from knox import views as knox_views

from main import (
    apigroup_views,
    views,
    auth_views,
    whiteflag_views,
    crypto_views,
    fennel_views,
    compound_views,
    api_admin_views,
    message_views,
    onetrust_views,
    trust_views,
)

# pylint: disable=invalid-name
app_name = "main"

urlpatterns = [
    path("", views.api_root),  # Root API endpoint
    path("get_version/", views.get_version),
    path("healthcheck/", views.healthcheck),
    path("livecheck/", views.livecheck),
    path("group/create/", api_admin_views.create_new_api_group),
    path("group/fennel_admin/get_list/", api_admin_views.get_api_group_list),
    path("group/add_user/", api_admin_views.add_user_to_api_group),
    path("group/remove_user/", api_admin_views.remove_user_from_api_group),
    path("group/add_admin/", api_admin_views.add_admin_to_api_group),
    path("group/remove_admin/", api_admin_views.remove_admin_from_api_group),
    path("group/generate_keypair/", apigroup_views.generate_apigroup_keypair),
    path("group/get_list/", apigroup_views.get_group_list),
    path("group/get_keypair/", apigroup_views.get_apigroup_keypair),
    path(
        "group/get_accounts_billable_count/",
        api_admin_views.get_accounts_billable_count,
    ),
    path(
        "group/get_api_group_requests_count/",
        api_admin_views.get_api_group_requests_count,
    ),
    path(
        "group/get_api_group_users/",
        api_admin_views.get_api_group_users,
    ),
    path(
        "group/get_join_requests/",
        api_admin_views.get_join_requests,
    ),
    path(
        "group/send_join_request/",
        api_admin_views.send_join_request,
    ),
    path(
        "group/accept_join_request/",
        api_admin_views.accept_join_request,
    ),
    path("whiteflag/healthcheck/", whiteflag_views.fennel_cli_healthcheck),
    path("fennel/healthcheck/", views.subservice_healthcheck),
    path("whiteflag/authenticate/", whiteflag_views.whiteflag_authenticate),
    path(
        "whiteflag/discontinue_authentication/",
        whiteflag_views.whiteflag_discontinue_authentication,
    ),
    path("whiteflag/encode/", whiteflag_views.whiteflag_encode),
    path("whiteflag/decode/", whiteflag_views.whiteflag_decode),
    path(
        "whiteflag/generate_encryption_key/<int:group_id>/",
        whiteflag_views.whiteflag_generate_shared_secret_key,
    ),
    path(
        "whiteflag/generate_shared_token/",
        whiteflag_views.whiteflag_generate_shared_token,
    ),
    path(
        "whiteflag/generate_public_token/",
        whiteflag_views.whiteflag_generate_public_token,
    ),
    path(
        "whiteflag/decode_list/",
        compound_views.decode_list,
    ),
    path(
        "whiteflag/encode_list/",
        compound_views.encode_list,
    ),
    path(
        "whiteflag/get_fee_for_send_signal_with_annotations/",
        compound_views.get_fee_for_send_signal_with_annotations,
    ),
    path(
        "whiteflag/get_fee_for_encode_and_send_signal/",
        compound_views.get_fee_for_encode_and_send_signal,
    ),
    path(
        "whiteflag/encode_and_send_signal/",
        compound_views.encode_and_send_signal,
    ),
    path(
        "whiteflag/send_signal_with_annotations/",
        compound_views.send_signal_with_annotations,
    ),
    path(
        "whiteflag/get_fee_for_discontinue_signal/<int:signal_id>/",
        compound_views.get_fee_for_discontinue_signal,
    ),
    path(
        "whiteflag/discontinue_signal/<int:signal_id>/",
        compound_views.discontinue_signal,
    ),
    path(
        "messages/get_messages/",
        message_views.get_messages,
    ),
    path(
        "messages/get_sent_messages/",
        message_views.get_sent_messages,
    ),
    path(
        "messages/get_messages/",
        message_views.get_messages,
    ),
    path(
        "messages/get_sent_messages/",
        message_views.get_sent_messages,
    ),
    path(
        "messages/get_message_by_id/<int:message_id>/",
        message_views.get_message_by_id,
    ),
    path(
        "messages/send_message/",
        message_views.send_message,
    ),
    path(
        "crypto/dh/whiteflag/is_this_encrypted/",
        crypto_views.wf_is_this_encrypted,
    ),
    path(
        "crypto/dh/generate_keypair/",
        crypto_views.generate_diffie_hellman_keypair,
    ),
    path(
        "crypto/dh/get_my_keypair/",
        crypto_views.get_my_keypair,
    ),
    path(
        "crypto/dh/get_shared_secret/",
        crypto_views.get_diffie_hellman_shared_secret,
    ),
    path(
        "crypto/dh/dm/encrypt_message/",
        crypto_views.dh_encrypt_message,
    ),
    path(
        "crypto/dh/dm/decrypt_message/",
        crypto_views.dh_decrypt_message,
    ),
    path(
        "crypto/dh/whiteflag/encrypt_message/",
        crypto_views.dh_encrypt_whiteflag_message,
    ),
    path(
        "crypto/dh/whiteflag/decrypt_message/",
        crypto_views.dh_decrypt_whiteflag_message,
    ),
    path(
        "crypto/dh/get_public_key_by_username/",
        crypto_views.get_dh_public_key_by_username,
    ),
    path(
        "crypto/dh/get_public_key_by_address/",
        crypto_views.get_dh_public_key_by_address,
    ),
    path("fennel/create_account/", fennel_views.create_account, name="create_account"),
    path(
        "onetrust/create_self_custodial_account/",
        onetrust_views.create_self_custodial_account,
    ),
    path(
        "onetrust/reconstruct_self_custodial_account/",
        onetrust_views.reconstruct_self_custodial_account,
    ),
    path(
        "onetrust/download_self_custodial_account_as_json/",
        onetrust_views.download_self_custodial_account_as_json,
    ),
    path(
        "onetrust/get_self_custodial_account_address/",
        onetrust_views.get_self_custodial_account_address,
    ),
    path("fennel/download_account_as_json/", fennel_views.download_account_as_json),
    path("fennel/get_account_balance/", fennel_views.get_account_balance),
    path("fennel/get_address/", fennel_views.get_address),
    path("fennel/get_fee_for_transfer_token/", fennel_views.get_fee_for_transfer_token),
    path("fennel/transfer_token/", fennel_views.transfer_token),
    path("fennel/get_fee_for_new_signal/", fennel_views.get_fee_for_new_signal),
    path("fennel/send_new_signal/", fennel_views.send_new_signal),
    path(
        "fennel/get_fee_for_send_signal_list/",
        compound_views.get_fee_for_send_signal_list,
    ),
    path("fennel/send_signal_list/", compound_views.send_signal_list),
    path("fennel/get_fee_for_sync_signal/", fennel_views.get_fee_for_sync_signal),
    path("fennel/sync_signal/", fennel_views.sync_signal),
    path("fennel/confirm_signal/", fennel_views.confirm_signal),
    path("fennel/search_signals/", fennel_views.search_signals),
    path("fennel/get_signal_by_id/<int:signal_id>/", fennel_views.get_signal_by_id),
    path("fennel/get_signals/", fennel_views.get_signals),
    path("fennel/get_signals/<int:count>/", fennel_views.get_signals),
    path(
        "fennel/get_signals_in_range/<int:start_index>/<int:end_index>/",
        fennel_views.get_signals_in_range,
    ),
    path("fennel/get_unsynced_signals/", fennel_views.get_unsynced_signals),
    path("fennel/get_fee_history/", fennel_views.get_fee_history),
    path("fennel/get_fee_history/<int:count>/", fennel_views.get_fee_history),
    path("trust/get_fee_for_issue_trust/", trust_views.get_fee_for_issue_trust),
    path("trust/issue_trust/", trust_views.issue_trust),
    path("trust/get_fee_for_remove_trust/", trust_views.get_fee_for_remove_trust),
    path("trust/remove_trust/", trust_views.remove_trust),
    path("trust/get_fee_for_request_trust/", trust_views.get_fee_for_request_trust),
    path("trust/request_trust/", trust_views.request_trust),
    path(
        "trust/get_fee_for_cancel_trust_request/",
        trust_views.get_fee_for_cancel_trust_request,
    ),
    path("trust/cancel_trust_request/", trust_views.cancel_trust_request),
    path("trust/get_trust_requests/", trust_views.get_trust_requests),
    path("trust/get_trust_connections/", trust_views.get_trust_connections),
    path("trust/check_if_trust_exists/", trust_views.check_if_trust_exists),
    path("auth/register/", auth_views.UserRegisterView.as_view()),
    path("auth/login/", auth_views.LoginAPIView.as_view()),
    path("auth/user/", auth_views.UserAPI.as_view()),
    path("auth/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("auth/change_password/", auth_views.ChangePasswordView.as_view()),
    path(
        "auth/reset_password/verify_token/",
        auth_views.CustomPasswordTokenVerificationView.as_view(),
    ),
    path(
        "auth/reset_password/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
