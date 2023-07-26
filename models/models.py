from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompt_library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

class Prompt(db.Model):
    __tablename__ = 'Prompt'

    id = db.Column('Prompt_ID', db.Integer, primary_key=True)
    text = db.Column('Prompt_Text', db.String)
    subcategory_id = db.Column('Subcategory_ID', db.Integer, db.ForeignKey('Subcategory.Subcategory_ID'))
    source_id = db.Column('Source_ID', db.Integer, db.ForeignKey('Source.Source_ID'))
    status = db.Column('Status', db.String)
    parent_id = db.Column('Parent_ID', db.Integer, db.ForeignKey('Prompt.Prompt_ID'))
    keywords = db.relationship('Keyword', secondary='prompt_keyword', backref=db.backref('prompts', lazy='dynamic'))

class Category(db.Model):
    __tablename__ = 'Category'

    id = db.Column('Category_ID', db.Integer, primary_key=True)
    name = db.Column('Category_Name', db.String)
    description = db.Column('Description', db.String)

class Subcategory(db.Model):
    __tablename__ = 'Subcategory'

    id = db.Column('Subcategory_ID', db.Integer, primary_key=True)
    name = db.Column('Subcategory_Name', db.String)
    description = db.Column('Description', db.String)
    category_id = db.Column('Category_ID', db.Integer, db.ForeignKey('Category.Category_ID'))

class Keyword(db.Model):
    __tablename__ = 'Keyword'

    id = db.Column('Keyword_ID', db.Integer, primary_key=True)
    name = db.Column('Keyword_Name', db.String)

class PromptKeyword(db.Model):
    __tablename__ = 'Prompt_Keyword'

    prompt_id = db.Column('Prompt_ID', db.Integer, db.ForeignKey('Prompt.Prompt_ID'), primary_key=True)
    keyword_id = db.Column('Keyword_ID', db.Integer, db.ForeignKey('Keyword.Keyword_ID'), primary_key=True)

class Usage(db.Model):
    __tablename__ = 'Usage'

    id = db.Column('Usage_ID', db.Integer, primary_key=True)
    prompt_id = db.Column('Prompt_ID', db.Integer, db.ForeignKey('Prompt.Prompt_ID'))
    user_id = db.Column('User_ID', db.Integer)
    access_date = db.Column('Access_Date', db.DateTime)

class Source(db.Model):
    __tablename__ = 'Source'

    id = db.Column('Source_ID', db.Integer, primary_key=True)
    name = db.Column('Source_Name', db.String)
    source_type = db.Column('Source_Type', db.String)
    description = db.Column('Description', db.String)
