def superhero(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

superhero(name="Ironman", power="jarvis")
superhero(name="Ironman")
superhero(name="Ironman", power="Jarvis", enemy="Thanos")