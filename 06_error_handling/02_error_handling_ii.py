def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        # using this will give error within error message
        # because we are concatenating the error message object to str
        # print("Please enter numbers " + err)

        # use this to display the error
        print(f"Exception raised: {err}")
        # or use this
        print(err)
    finally:
        print("Thank you")


print(sum(1, 0))
