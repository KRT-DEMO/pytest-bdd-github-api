import uuid
from faker import Faker
fake = Faker()

class Builder:
    @staticmethod
    def build_repo():
        repository = {
            'name': uuid.uuid4().hex,
            'description': fake.text(),
            'homepage': 'https://github.com',
            'private': False,
            'has_issues': True,
            'has_projects': True,
            'has_wiki': True,
            'is_template': False,
            'auto_init': True,
            'gitignore_template': 'VisualStudio',
            'license_template': 'mit',
            'allow_squash_merge': True,
            'allow_merge_commit': True,
            'allow_rebase_merge': True
        }
        return repository
