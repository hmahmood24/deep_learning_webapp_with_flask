from webapp import webapp

if __name__=="__main__":
    webapp.debug = True
    webapp.run(host="0.0.0.0", port="5000")