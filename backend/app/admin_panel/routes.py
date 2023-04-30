from app import db, admin
from app.models import Map
from app.admin_panel.views import MapView, LogoutMenuLink


# Add view
admin.add_view(MapView(Map, db.session, name="Данные участков"))
admin.add_link(LogoutMenuLink(name='Выход', category='', url="/logout"))