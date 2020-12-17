
def init_app(app):
    """Inicialização das extensões"""
    
    @app.route('/')
    def index():
        return 'Welcome to all0cer delivery'
    
    
    
    @app.route('/bebidas')
    def bebidas():
        return 'Açai, Vinho, Água'
