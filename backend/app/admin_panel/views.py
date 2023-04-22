import os
from flask_admin.contrib.sqla import ModelView

file_path = os.path.abspath(os.path.dirname(__name__))

class MapView(ModelView):
    column_labels = {
        'kadastr_id': 'Кадастровый id',
        'square': 'Площадь',
        'kadastr_number': 'Кадастровый номер',
    }

    # поля формы создания и редактирования
    form_columns = ('kadastr_id', 'square', 'kadastr_number')

    # поля вывода
    column_list = ('kadastr_id', 'square', 'kadastr_number')

    column_editable_list = ('kadastr_id', 'square', 'kadastr_number')
    column_default_sort = ('kadastr_id', True)
    column_searchable_list = ['kadastr_id', 'kadastr_number']

    export_max_rows = 500
    export_types = ['csv']
    form_widget_args = {
        'date': {
            'style': 'max-width: 200px;'
        },
    }


    create_template = 'admin/map_create.html'
    edit_template = 'admin/map_edit.html'
