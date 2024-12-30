print("Whenever an applciatin is build, when the aplciation si build, by dev team and sent it to the testing team, and they igure out any mimatch b/w execpeted adn actual output, they call is as 'Defect' and report it to teh dev team. If teh dev team, figured out, tha was actually an issue, then thery call it as 'Bug', if both dev team adn testign team, didnt find ay issues nad the end uder at prodcuton,finds any issue,it's called 'Error'")
print("Assertions are sued for error debugging, unlike print statements, we can turn on/off assertions using -O flag, so in prod., env., we would turn off the assertions, we don't want the users to see the error debugging statements, and also unlike print statements, it will not print the debugging statement, along with the actual display content.There are 2 types of assertions: \n 1. Simple assertion: It will have only the assert conditinla statement, it rasises assertion errroe, when the condition fails. \n 2. Augmented assertion: Here, if the assertion condtion fails, it prints description as output. assert conditional_Statement,description. Whenever the conditonla staemetn in assert fails, it will lead assertion error.")

def prediction_simple_assertion(correct_pred,total_samples):
    accuracy = correct_pred/total_samples
    print(r'To remove the assertions, use python -O "C:\\Users\\HP\\Documents\\Python_OOPs\\19. Assertions.py" ')
    assert accuracy>0.5

    print("Weather Forecasting being done....")





prediction_simple_assertion(5,10)
