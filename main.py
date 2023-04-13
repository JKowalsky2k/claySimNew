import engine.engine as engine
import security

if __name__ == "__main__":
    security_defender = security.Security()
    if True == security_defender.check():
        app = engine.Engine()
        app.run()
        print(f'{app.__str__() = }')
    else:
        print("[Error] Licence problem, sorry.")
        input("Press ENTER to continue...")