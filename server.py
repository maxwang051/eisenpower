from views import app
import os

PORT = int(os.getenv('PORT', 8080))
app.run(debug=True, port=PORT)
