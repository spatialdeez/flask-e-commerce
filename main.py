from website import create_app

app = create_app()

# Only run the website instance if its run from main.py
if __name__ == '__main__':
    app.run(debug=True)
    # There are other parameters could be used: 
    # host: run the website on specific ip address. leave blank to default (usually localhost)
    # port: specify which port to run the website on.