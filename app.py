from flask import Flask, request
from flask_restful import Resource, Api
from models.models import setup_db, db, Prompt, Category, Subcategory, Keyword, PromptKeyword, Usage, Source
def create_app():
    app = Flask(__name__)
    api = Api(app)
    setup_db(app)
    with app.app_context():
        db.create_all()

    class PromptResource(Resource):
        def get(self, id=None):
            if id:
                prompt = Prompt.query.get(id)
                if prompt:
                    return {'id': prompt.id, 'text': prompt.text}
                else:
                    return {'error': 'Prompt not found'}, 404
            prompts = Prompt.query.all()
            return [{'id': prompt.id, 'text': prompt.text} for prompt in prompts]

        def post(self):
            data = request.get_json()
            new_prompt = Prompt(text=data['text'])
            db.session.add(new_prompt)
            db.session.commit()
            return {'id': new_prompt.id, 'text': new_prompt.text}, 201

        def put(self, id):
            data = request.get_json()
            prompt = Prompt.query.get(id)
            if prompt:
                prompt.text = data['text']
                db.session.commit()
                return {'id': prompt.id, 'text': prompt.text}
            else:
                return {'error': 'Prompt not found'}, 404

        def delete(self, id):
            prompt = Prompt.query.get(id)
            if prompt:
                db.session.delete(prompt)
                db.session.commit()
                return {'result': 'Prompt deleted'}
            else:
                return {'error': 'Prompt not found'}, 404

    api.add_resource(PromptResource, '/prompts', '/prompts/<int:id>')

    # <Generate the rest of the resources below this line>
    class CategoryResource(Resource):
        def get(self, id=None):
            if id:
                category = Category.query.get(id)
                if category:
                    return {'id': category.id, 'name': category.name}
                else:
                    return {'error': 'Category not found'}, 404
            categories = Category.query.all()
            return [{'id': category.id, 'name': category.name} for category in categories]

        def post(self):
            data = request.get_json()
            new_category = Category(name=data['name'])
            db.session.add(new_category)
            db.session.commit()
            return {'id': new_category.id, 'name': new_category.name}, 201

        def put(self, id):
            data = request.get_json()
            category = Category.query.get(id)
            if category:
                category.name = data['name']
                db.session.commit()
                return {'id': category.id, 'name': category.name}
            else:
                return {'error': 'Category not found'}, 404

        def delete(self, id):
            category = Category.query.get(id)
            if category:
                db.session.delete(category)
                db.session.commit()
                return {'result': 'Category deleted'}
            else:
                return {'error': 'Category not found'}, 404

    api.add_resource(CategoryResource, '/categories', '/categories/<int:id>')

    class SubcategoryResource(Resource):
        def get(self, id=None):
            if id:
                subcategory = Subcategory.query.get(id)
                if subcategory:
                    return {'id': subcategory.id, 'name': subcategory.name}
                else:
                    return {'error': 'Subcategory not found'}, 404
            subcategories = Subcategory.query.all()
            return [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]

        def post(self):
            data = request.get_json()
            new_subcategory = Subcategory(name=data['name'])
            db.session.add(new_subcategory)
            db.session.commit()
            return {'id': new_subcategory.id, 'name': new_subcategory.name}, 201

        def put(self, id):
            data = request.get_json()
            subcategory = Subcategory.query.get(id)
            if subcategory:
                subcategory.name = data['name']
                db.session.commit()
                return {'id': subcategory.id, 'name': subcategory.name}
            else:
                return {'error': 'Subcategory not found'}, 404

        def delete(self, id):
            subcategory = Subcategory.query.get(id)
            if subcategory:
                db.session.delete(subcategory)
                db.session.commit()
                return {'result': 'Subcategory deleted'}
            else:
                return {'error': 'Subcategory not found'}, 404

    api.add_resource(SubcategoryResource, '/subcategories', '/subcategories/<int:id>')

    class KeywordResource(Resource):
        def get(self, id=None):
            if id:
                keyword = Keyword.query.get(id)
                if keyword:
                    return {'id': keyword.id, 'name': keyword.name}
                else:
                    return {'error': 'Keyword not found'}, 404
            keywords = Keyword.query.all()
            return [{'id': keyword.id, 'name': keyword.name} for keyword in keywords]

        def post(self):
            data = request.get_json()
            new_keyword = Keyword(name=data['name'])
            db.session.add(new_keyword)
            db.session.commit()
            return {'id': new_keyword.id, 'name': new_keyword.name}, 201

        def put(self, id):
            data = request.get_json()
            keyword = Keyword.query.get(id)
            if keyword:
                keyword.name = data['name']
                db.session.commit()
                return {'id': keyword.id, 'name': keyword.name}
            else:
                return {'error': 'Keyword not found'}, 404

        def delete(self, id):
            keyword = Keyword.query.get(id)
            if keyword:
                db.session.delete(keyword)
                db.session.commit()
                return {'result': 'Keyword deleted'}
            else:
                return {'error': 'Keyword not found'}, 404

    api.add_resource(KeywordResource, '/keywords', '/keywords/<int:id>')

    class PromptKeywordResource(Resource):
        def get(self, id=None):
            if id:
                prompt_keyword = PromptKeyword.query.get(id)
                if prompt_keyword:
                    return {'id': prompt_keyword.id, 'prompt_id': prompt_keyword.prompt_id, 'keyword_id': prompt_keyword.keyword_id}
                else:
                    return {'error': 'Prompt_Keyword not found'}, 404
            prompt_keywords = PromptKeyword.query.all()
            return [{'id': prompt_keyword.id, 'prompt_id': prompt_keyword.prompt_id, 'keyword_id': prompt_keyword.keyword_id} for prompt_keyword in prompt_keywords]

        def post(self):
            data = request.get_json()
            new_prompt_keyword = PromptKeyword(prompt_id=data['prompt_id'], keyword_id=data['keyword_id'])
            db.session.add(new_prompt_keyword)
            db.session.commit()
            return {'id': new_prompt_keyword.id, 'prompt_id': new_prompt_keyword.prompt_id, 'keyword_id': new_prompt_keyword.keyword_id}, 201

        def put(self, id):
            data = request.get_json()
            prompt_keyword = PromptKeyword.query.get(id)
            if prompt_keyword:
                prompt_keyword.prompt_id = data['prompt_id']
                prompt_keyword.keyword_id = data['keyword_id']
                db.session.commit()
                return {'id': prompt_keyword.id, 'prompt_id': prompt_keyword.prompt_id, 'keyword_id': prompt_keyword.keyword_id}
            else:
                return {'error': 'Prompt_Keyword not found'}, 404

        def delete(self, id):
            prompt_keyword = PromptKeyword.query.get(id)
            if prompt_keyword:
                db.session.delete(prompt_keyword)
                db.session.commit()
                return {'result': 'Prompt_Keyword deleted'}
            else:
                return {'error': 'Prompt_Keyword not found'}, 404

    api.add_resource(PromptKeywordResource, '/prompt_keywords', '/prompt_keywords/<int:id>')

    class UsageResource(Resource):
        def get(self, id=None):
            if id:
                usage = Usage.query.get(id)
                if usage:
                    return {'id': usage.id, 'prompt_id': usage.prompt_id, 'user_id': usage.user_id, 'access_date': usage.access_date}
                else:
                    return {'error': 'Usage not found'}, 404
            usages = Usage.query.all()
            return [{'id': usage.id, 'prompt_id': usage.prompt_id, 'user_id': usage.user_id, 'access_date': usage.access_date} for usage in usages]

        def post(self):
            data = request.get_json()
            new_usage = Usage(prompt_id=data['prompt_id'], user_id=data['user_id'], access_date=data['access_date'])
            db.session.add(new_usage)
            db.session.commit()
            return {'id': new_usage.id, 'prompt_id': new_usage.prompt_id, 'user_id': new_usage.user_id, 'access_date': new_usage.access_date}, 201

        def put(self, id):
            data = request.get_json()
            usage = Usage.query.get(id)
            if usage:
                usage.prompt_id = data['prompt_id']
                usage.user_id = data['user_id']
                usage.access_date = data['access_date']
                db.session.commit()
                return {'id': usage.id, 'prompt_id': usage.prompt_id, 'user_id': usage.user_id, 'access_date': usage.access_date}
            else:
                return {'error': 'Usage not found'}, 404

        def delete(self, id):
            usage = Usage.query.get(id)
            if usage:
                db.session.delete(usage)
                db.session.commit()
                return {'result': 'Usage deleted'}
            else:
                return {'error': 'Usage not found'}, 404

    api.add_resource(UsageResource, '/usages', '/usages/<int:id>')

    class SourceResource(Resource):
        def get(self, id=None):
            if id:
                source = Source.query.get(id)
                if source:
                    return {'id': source.id, 'name': source.name, 'source_type': source.source_type, 'description': source.description}
                else:
                    return {'error': 'Source not found'}, 404
            sources = Source.query.all()
            return [{'id': source.id, 'name': source.name, 'source_type': source.source_type, 'description': source.description} for source in sources]

        def post(self):
            data = request.get_json()
            new_source = Source(name=data['name'], source_type=data['source_type'], description=data['description'])
            db.session.add(new_source)
            db.session.commit()
            return {'id': new_source.id, 'name': new_source.name, 'source_type': new_source.source_type, 'description': new_source.description}, 201

        def put(self, id):
            data = request.get_json()
            source = Source.query.get(id)
            if source:
                source.name = data['name']
                source.source_type = data['source_type']
                source.description = data['description']
                db.session.commit()
                return {'id': source.id, 'name': source.name, 'source_type': source.source_type, 'description': source.description}
            else:
                return {'error': 'Source not found'}, 404

        def delete(self, id):
            source = Source.query.get(id)
            if source:
                db.session.delete(source)
                db.session.commit()
                return {'result': 'Source deleted'}
            else:
                return {'error': 'Source not found'}, 404

    api.add_resource(SourceResource, '/sources', '/sources/<int:id>')

    return app

if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
