from django.conf.urls import url

from awx.api.views import WebhookKeyView, GithubWebhookReceiver, GitlabWebhookReceiver, GiteaWebhookReceiver


urlpatterns = [
    url(r'^webhook_key/$', WebhookKeyView.as_view(), name='webhook_key'),
    url(r'^github/$', GithubWebhookReceiver.as_view(), name='webhook_receiver_github'),
    url(r'^gitlab/$', GitlabWebhookReceiver.as_view(), name='webhook_receiver_gitlab'),
    url(r'^gitea/$', GiteaWebhookReceiver.as_view(), name='webhook_receiver_gitea'),
]
