from website import create_app

app = create_app()

# only if we run this file, run the application in debug mode.  Anytime that we change the code, it will rerun the website server. 
# We will only enable the debug feature when in development.  We will not have it in production. 
if __name__ == '__main__':
    app.run(debug=True)