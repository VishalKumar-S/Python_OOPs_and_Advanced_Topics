def prediction_augmented_assertion(correct_pred,total_samples):
    accuracy = correct_pred/total_samples
    
    assert accuracy>0.5,'Model is performing worse than a random guess. Pls check the last model update and batch data quality. To remove this assertions, use python -O "C:\\Users\\HP\\Documents\\Python_OOPs\\19.1).augmented_Assertions.py"'

    print("Weather Forecasting being done....")


prediction_augmented_assertion(4,15)
