from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import Base.routing
# Like the urlpatterns we use this ProtocolTypeRouter
# Meaning when we get our web socket request this is how to route it

application = ProtocolTypeRouter({
            # For using the authentication of django
            'websocket':AuthMiddlewareStack(
                URLRouter(
                    # Here we have included the patterns inside our Base app
                    Base.routing.websocket_urlpatterns
                )
            )

})