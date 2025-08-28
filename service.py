class Service:

    def __init__(self, url):
        self._base_url = url.rstrip('/')

    @property
    def main(self):
        return f'{self._base_url}'
    
    @property
    def signin(self):
        return f'{self._base_url}/signin'
    
    @property
    def signup(self):
        return f'{self._base_url}/signup'
    
    @property
    def recipes(self):
        return f'{self._base_url}/recipes'

site = Service('https://foodgram-frontend-1.prakticum-team.ru')