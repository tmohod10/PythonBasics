while True:
    try:
        age = int(input("What is your age? "))
        if age <= 0:
            raise ValueError("Hey cut it out")
        10 / age
    except ValueError as err:
        print(f"ValueError exception is raised: {err}")
    else:
        break
    finally:
        print("Thank you")

