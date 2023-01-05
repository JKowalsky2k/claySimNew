import engine

if __name__ == "__main__":
    app = engine.Engine()
    app.run()
    print(f'{app.__str__() = }')