from flask import Flask

import flask_admin
from flask_admin.contrib import peewee as flask_admin_peewee

import peewee

import book_db

app = Flask(__name__)

# 시크릿 키 설정
app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

class PublisherAdmin(flask_admin_peewee.ModelView):
    """publisher 테이블 관리 화면 전용 클래스"""
    column_display_pk = True
    column_sortable_list = ('id', 'name', 'is_active')
    column_filters = column_sortable_list
    column_editable_list = ('name', 'is_active')
    form_columns = column_sortable_list

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.save(force_insert=True)

@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    # 관리 화면 전용 객체 생성
    admin = flask_admin.Admin(app, name='Example: Peewee')

    # publisher 테이블 전용 관리 화면 추가
    admin.add_view(PublisherAdmin(book_db.Publisher))

    app.run(debug=True)
